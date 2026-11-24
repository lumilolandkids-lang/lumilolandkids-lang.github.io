#!/usr/bin/env python3
"""Publish ONE old ready-but-unpublished video per day (her rule, 24 Nov 2026:
"كل الفيديوهات القديمه الي جاهزه قديما وما نزلت نزلوها كل يوم").

Usage: python3 backlog.py            -> publish the next pending item of log/backlog.json (once per New York day)
       python3 backlog.py --status   -> show the queue
Item kinds: "rebuild" = download the saved C1 shots (jobs/<slug>/shots.json), rebuild with montage.py
(or the job's rebuild.sh), upload PUBLIC at once with upload_ready.py; "make_public" = the video is already on
YouTube as private -> set it public. 0 ViewMax credits. Never twice: done items keep their url.
"""
import datetime, json, subprocess, sys
from pathlib import Path
from zoneinfo import ZoneInfo
import pipeline as P

ROOT = Path(__file__).resolve().parent
Q = ROOT / "log" / "backlog.json"


def sh(cmd):
    print("+", cmd, flush=True)
    subprocess.run(cmd, shell=True, check=True, cwd=ROOT)


def rebuild(slug):
    J = ROOT / "jobs" / slug
    if (J / "rebuild.sh").exists():
        sh(f"bash jobs/{slug}/rebuild.sh")
        return
    edit = json.loads((J / "edit.json").read_text())
    W = ROOT / edit["workdir"]
    W.mkdir(parents=True, exist_ok=True)
    shots = json.loads((J / "shots.json").read_text())
    for n in sorted({c["shot"] for c in edit["cuts"]}):
        out = W / f"shot{n}.mp4"
        if not out.exists() or out.stat().st_size == 0:
            sh(f"curl -sSL --retry 4 -o {out} '{shots[f'shot{n}']}'")
    song = edit.get("song")
    if song and not (ROOT / song).exists() and not (W / song).exists():
        sh(f"cp jobs/{slug}/song.mp3 {W}/song.mp3")
    sh(f"python3 montage.py build jobs/{slug}/edit.json")
    sh(f"python3 montage.py motion {edit['workdir']}/{edit.get('out', 'final.mp4')} | tail -1")
    job = json.loads((ROOT / "jobs" / f"{slug}.json").read_text())
    (ROOT / "ready").mkdir(exist_ok=True)
    sh(f"cp {edit['workdir']}/{edit.get('out', 'final.mp4')} {job['video']}")


def make_public(vid):
    t = P.yt_token()
    H = {"Authorization": "Bearer " + t}
    c, b, _ = P.http(f"https://www.googleapis.com/youtube/v3/videos?part=status&id={vid}", headers=H)
    st = json.loads(b)["items"][0]["status"]
    body = {"id": vid, "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": True,
                                  "containsSyntheticMedia": True, "embeddable": st.get("embeddable", True),
                                  "license": st.get("license", "youtube"), "publicStatsViewable": st.get("publicStatsViewable", True)}}
    c, b, _ = P.http("https://www.googleapis.com/youtube/v3/videos?part=status", body, H, method="PUT")
    print("[make_public] HTTP", c, b[:200])
    if c != 200:
        raise SystemExit(f"make_public failed HTTP {c}")
    return f"https://youtube.com/shorts/{vid}"


def main():
    q = json.loads(Q.read_text())
    if "--status" in sys.argv:
        for it in q["items"]:
            print(it.get("done") or "pending", "|", it["slug"], "|", it.get("url", ""))
        return 0
    today = datetime.datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    if any(it.get("done") == today for it in q["items"]) and "--force" not in sys.argv:
        print(f"[backlog] already published one today ({today}) - nothing to do")
        return 0
    pending = [it for it in q["items"] if not it.get("done")]
    if not pending:
        print("[backlog] queue empty - all old videos are published")
        return 0
    it = pending[0]
    print(f"[backlog] next: {it['slug']} ({it['kind']})")
    if it["kind"] == "make_public":
        url = make_public(it["youtube_id"])
    else:
        rebuild(it["slug"])
        out = subprocess.run(["python3", "upload_ready.py", f"jobs/{it['slug']}.json"], cwd=ROOT,
                             capture_output=True, text=True)
        print(out.stdout[-1500:], out.stderr[-1500:])
        urls = [l.split()[-1] for l in out.stdout.splitlines() if l.startswith("[upload] ")]
        if out.returncode or not urls:
            raise SystemExit("[backlog] upload failed - fix and retry (check log/videos.jsonl for a video id first)")
        url = urls[-1]
        job = json.loads((ROOT / "jobs" / f"{it['slug']}.json").read_text())
        Path(ROOT / job["video"]).unlink(missing_ok=True)
    it.update(done=today, url=url)
    Q.write_text(json.dumps(q, ensure_ascii=False, indent=1))
    print(f"[backlog] PUBLISHED {it['slug']} -> {url}  ({len(pending) - 1} left)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
