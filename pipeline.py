#!/usr/bin/env python3
"""Crayon Babies video autopilot: clips -> music (Lyria) -> ffmpeg edit -> YouTube upload -> log.

Usage: python3 pipeline.py job.json [--no-upload]

job.json (written by the scheduled Claude session after generating clips in ViewMax):
{
  "idea": "...", "title": "...", "description": "...", "tags": ["..."],
  "shot_prompts": ["...", "...", "..."],
  "clips": ["https://...mp4", "https://...mp4", "https://...mp4"],
  "viewmax_credits_before": 8143, "viewmax_credits_used": 120
}

Exit codes: 0 ok, 2 bad input, 3 Gemini billing/quota (402/429), 4 other API error, 5 ffmpeg error.
"""
import base64, datetime, json, os, subprocess, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG = ROOT / "log" / "videos.jsonl"
GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent?key=" + os.environ.get("GEMINI_API_KEY", "")
TEXT_MODELS = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash"]
MUSIC_MODELS = ["lyria-3-clip-preview", "lyria-3.5"]
W, H, FPS, XFADE = 1080, 1920, 30, 0.5
MUSIC_VOL, CLIP_VOL, FADE_IN, FADE_OUT = 0.9, 0.25, 1.0, 2.0


class BillingError(Exception):
    pass


def http(url, data=None, headers=None, method=None):
    body = json.dumps(data).encode() if isinstance(data, (dict, list)) else data
    h = {"Content-Type": "application/json"} if isinstance(data, (dict, list)) else {}
    h.update(headers or {})
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.status, r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers)


def gemini(models, parts, retries=3):
    """Call generateContent, falling back across models on 503. Raises BillingError on 402/429."""
    last = None
    for model in models:
        for attempt in range(retries):
            code, body, _ = http(GEMINI.format(model), {"contents": [{"parts": parts}]})
            if code == 200:
                return model, json.loads(body)
            last = f"{model} HTTP {code}: {body[:400].decode(errors='replace')}"
            if code in (402, 429):
                raise BillingError(last)
            if code in (500, 503):
                time.sleep(5 * (attempt + 1))
                continue
            break  # 404 etc: try next model
    raise RuntimeError(last)


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        raise subprocess.CalledProcessError(p.returncode, cmd, p.stdout, p.stderr[-2000:])
    return p.stdout


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]))


def has_audio(path):
    return bool(run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", str(path)]).strip())


def download(clips, work):
    out = []
    for i, url in enumerate(clips):
        p = work / f"clip{i}.mp4"
        if not p.exists():
            code, body, _ = http(url)
            if code != 200:
                raise RuntimeError(f"download clip {i}: HTTP {code}")
            p.write_bytes(body)
        out.append(p)
    return out


def normalize(clips, work):
    """Scale/crop every clip to 1080x1920@30 with a stereo audio track (silent if missing)."""
    out = []
    for i, c in enumerate(clips):
        p = work / f"norm{i}.mp4"
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p,setsar=1"
        cmd = ["ffmpeg", "-y", "-i", str(c)]
        if not has_audio(c):
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-shortest"]
        cmd += ["-vf", vf, "-map", "0:v:0", "-map", "0:a:0" if has_audio(c) else "1:a:0",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-ar", "48000", "-ac", "2", str(p)]
        run(cmd)
        out.append(p)
    return out


def frames(clips, work):
    out = []
    for i, c in enumerate(clips):
        p = work / f"frame{i}.jpg"
        run(["ffmpeg", "-y", "-ss", f"{duration(c) / 2:.2f}", "-i", str(c), "-frames:v", "1", "-vf", "scale=540:-2", str(p)])
        out.append(p)
    return out


def music_prompt(frame_files, job):
    parts = [{"text": (
        "These are frames from a short 3D-animated video for toddlers featuring two babies, Jimmy and Eva. "
        f"Story idea: {job['idea']}\n"
        "Write ONE prompt (max 60 words) for an AI music generator describing a fitting background track: "
        "genre, mood, tempo in BPM, 3-4 instruments, how energy evolves. Instrumental only, no vocals, "
        "warm and child-friendly. Reply with the prompt text only.")}]
    for f in frame_files:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(f.read_bytes()).decode()}})
    model, resp = gemini(TEXT_MODELS, parts)
    return model, resp["candidates"][0]["content"]["parts"][0]["text"].strip()


def make_music(prompt, work):
    model, resp = gemini(MUSIC_MODELS, [{"text": prompt}])
    for part in resp["candidates"][0]["content"]["parts"]:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("mimeType", inline.get("mime_type", "")).startswith("audio"):
            ext = {"audio/mpeg": "mp3", "audio/mp3": "mp3", "audio/wav": "wav", "audio/x-wav": "wav"}.get(
                inline.get("mimeType", inline.get("mime_type")), "bin")
            p = work / f"music.{ext}"
            p.write_bytes(base64.b64decode(inline["data"]))
            return model, p
    raise RuntimeError(f"{model}: no audio in response: {json.dumps(resp)[:400]}")


def edit(norm, music, work):
    """Crossfade clips, lay music under the clip audio with fades, normalise loudness."""
    durs = [duration(c) for c in norm]
    total = sum(durs) - XFADE * (len(norm) - 1)
    inputs, fc = [], []
    for c in norm:
        inputs += ["-i", str(c)]
    inputs += ["-i", str(music)]
    v, a, offset = "[0:v]", "[0:a]", 0.0
    for i in range(1, len(norm)):
        offset += durs[i - 1] - XFADE
        fc.append(f"{v}[{i}:v]xfade=transition=fade:duration={XFADE}:offset={offset:.3f}[v{i}]")
        fc.append(f"{a}[{i}:a]acrossfade=d={XFADE}[a{i}]")
        v, a = f"[v{i}]", f"[a{i}]"
    m = len(norm)
    fc.append(f"{a}volume={CLIP_VOL}[clipa]")
    fc.append(f"[{m}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d={FADE_IN},"
              f"afade=t=out:st={total - FADE_OUT:.3f}:d={FADE_OUT},volume={MUSIC_VOL}[mus]")
    fc.append("[clipa][mus]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
    out = work / "final.mp4"
    run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", v, "-map", "[aout]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-t", f"{total:.3f}", str(out)])
    return out, total


def yt_token():
    code, body, _ = http("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
        "client_id": os.environ["YT_CLIENT_ID"], "client_secret": os.environ["YT_CLIENT_SECRET"],
        "refresh_token": os.environ["YT_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode(),
        {"Content-Type": "application/x-www-form-urlencoded"})
    if code != 200:
        raise RuntimeError(f"YouTube token refresh HTTP {code}: {body[:300]!r}")
    return json.loads(body)["access_token"]


def upload(video, job):
    token = yt_token()
    tags = [t.lstrip("#") for t in job.get("tags", [])]
    hashtags = " ".join("#" + t.replace(" ", "") for t in tags[:5])
    meta = {
        "snippet": {"title": job["title"][:100], "description": f"{job['description']}\n\n{hashtags}"[:5000],
                    "tags": tags, "categoryId": "1", "defaultLanguage": "en", "defaultAudioLanguage": "en"},
        "status": {"privacyStatus": job.get("privacy", "public"), "selfDeclaredMadeForKids": True,
                   "containsSyntheticMedia": True, "embeddable": True},
    }
    size = video.stat().st_size
    code, body, headers = http(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", meta,
        {"Authorization": f"Bearer {token}", "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    loc = {k.lower(): v for k, v in headers.items()}.get("location")
    if code != 200 or not loc:
        raise RuntimeError(f"YouTube upload init HTTP {code}: {body[:400]!r}")
    code, body, _ = http(loc, video.read_bytes(), {"Authorization": f"Bearer {token}", "Content-Type": "video/mp4"}, "PUT")
    if code not in (200, 201):
        raise RuntimeError(f"YouTube upload HTTP {code}: {body[:400]!r}")
    return json.loads(body)["id"]


def log(entry):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    job_path = Path(sys.argv[1])
    job = json.loads(job_path.read_text())
    work = ROOT / "runs" / job_path.stem
    work.mkdir(parents=True, exist_ok=True)
    entry = {"time": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
             "idea": job.get("idea"), "title": job.get("title"), "clips": job.get("clips"),
             "viewmax_credits_used": job.get("viewmax_credits_used"), "status": "started"}
    try:
        clips = normalize(download(job["clips"], work), work)
        tm, mprompt = music_prompt(frames(clips, work), job)
        print(f"[music prompt via {tm}] {mprompt}")
        mm, music = make_music(mprompt, work)
        print(f"[music via {mm}] {music}")
        final, total = edit(clips, music, work)
        entry.update(music_prompt=mprompt, music_model=mm, duration_s=round(total, 1), file=str(final))
        print(f"[edit] {final} ({total:.1f}s)")
        if "--no-upload" in sys.argv:
            entry["status"] = "edited (no upload)"
        else:
            vid = upload(final, job)
            entry.update(status="uploaded", youtube_id=vid, url=f"https://youtube.com/shorts/{vid}")
            print(f"[upload] https://youtube.com/shorts/{vid}")
        log(entry)
        return 0
    except BillingError as e:
        entry.update(status="failed: gemini billing/quota", error=str(e))
        log(entry)
        print("GEMINI BILLING/QUOTA ERROR (402/429): top up $5 for Gemini API on project Video Autopilot.\n" + str(e))
        return 3
    except subprocess.CalledProcessError as e:
        entry.update(status="failed: ffmpeg", error=e.stderr)
        log(entry)
        print("FFMPEG ERROR:\n" + e.stderr)
        return 5
    except Exception as e:
        entry.update(status="failed", error=str(e))
        log(entry)
        print(f"ERROR: {e}")
        return 4


if __name__ == "__main__":
    sys.exit(main())
