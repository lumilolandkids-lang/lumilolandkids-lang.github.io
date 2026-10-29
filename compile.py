#!/usr/bin/env python3
"""Crayon Babies weekly compilation (16:9 long video) and YouTube thumbnails.

  python3 compile.py build LIST.json OUT.mp4
  python3 compile.py thumb VIDEO.mp4 SECONDS "2-4 WORDS" OUT.jpg [YCENTER 0-1, default 0.55]

LIST.json
{
  "hook": {"file": "runs/compile/a/final.mp4", "start": 0.0, "dur": 4.0},   # strongest hook of the week (first!)
  "title": "This Week's Songs!",                                           # intro card text
  "episodes": [{"file": "runs/compile/a/final.mp4", "title": "Baby Lion Can't Roar!"}, ...]
}
Order (channel bible, section 11): hook clip -> intro card -> "Episode N" card + episode ... -> SUBSCRIBE outro.
Vertical Shorts are centred on a blurred copy of themselves (1920x1080, 24 fps). Cards get a soft chime.
Writes OUT.mp4 and OUT.chapters.txt (YouTube chapters: first at 0:00, each >= 10 s) for the description.

thumb: 1280x720 JPG < 2 MB from the frame at SECONDS (vertical videos are blur-filled), with 2-4 huge words in
Poppins Bold yellow with a purple border (section 10: big faces, strong emotion, 2-4 words).
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONT = ROOT / "assets" / "Poppins-Bold.ttf"
W, H, FPS = 1920, 1080, 24
ENC = ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]
BLURFILL = (f"split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=40,"
            f"eq=brightness=-0.06:saturation=1.1[bg];[b]scale=-2:{H}[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,"
            f"setsar=1,fps={FPS},format=yuv420p")
CHIME = ("aevalsrc='0.35*sin(2*PI*1318.5*t)*exp(-5*t)+0.28*sin(2*PI*1760*t)*exp(-5*(t-0.13))*gte(t,0.13)"
         "|0.35*sin(2*PI*1318.5*t)*exp(-5*t)+0.28*sin(2*PI*1760*t)*exp(-5*(t-0.13))*gte(t,0.13)':s=48000:d={d}")


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.stderr.write(p.stderr[-3000:])
        raise SystemExit("ffmpeg failed")
    return p.stdout


def dur(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]))


def frames(path):
    return int(run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v", "-show_entries",
                    "stream=nb_read_frames", "-of", "csv=p=0", str(path)]).strip())


def text_filter(txtfile, size, y, color="0xFFD21F", border="0x5B2A86", bw=12):
    return (f"drawtext=fontfile={FONT}:textfile={txtfile}:fontcolor={color}:borderw={bw}:bordercolor={border}:"
            f"fontsize={size}:x=(w-text_w)/2:y={y}")


def episode_part(src, out, start=None, length=None):
    pre = (["-ss", str(start)] if start is not None else []) + (["-t", str(length)] if length else [])
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", *pre, "-i", str(src), "-filter_complex",
         f"[0:v]{BLURFILL}[v];[0:a]aresample=48000,aformat=channel_layouts=stereo[a]", "-map", "[v]", "-map", "[a]",
         *ENC, str(out)])


def card(bg_src, out, lines, seconds, tmp, subscribe=False):
    """Blurred still from bg_src + big text lines (+ a red SUBSCRIBE button) + chime."""
    still = tmp / (out.stem + "_bg.png")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", "1.0", "-i", str(bg_src), "-frames:v", "1", "-vf",
         f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},gblur=sigma=30,eq=brightness=-0.12",
         str(still)])
    vf = []
    sizes = [150, 96, 80]
    ys = ["h*0.30", "h*0.52", "h*0.66"] if not subscribe else ["h*0.18", "h*0.36", "h*0.50"]
    for k, line in enumerate(lines[:3]):
        f = tmp / f"{out.stem}_{k}.txt"
        f.write_text(line)
        vf.append(text_filter(f, sizes[k], ys[k], color="0xFFD21F" if k == 0 else "white"))
    if subscribe:
        f = tmp / f"{out.stem}_btn.txt"
        f.write_text("SUBSCRIBE")
        vf.append("drawbox=x=(iw-620)/2:y=ih*0.68:w=620:h=150:color=0xE62117@1:t=fill")
        vf.append(f"drawtext=fontfile={FONT}:textfile={f}:fontcolor=white:fontsize=84:x=(w-text_w)/2:"
                  f"y=h*0.68+(150-text_h)/2")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-t", str(seconds),
         "-i", str(still), "-f", "lavfi", "-i", CHIME.format(d=seconds), "-vf",
         ",".join(vf + ["setsar=1", "format=yuv420p"]), "-shortest", *ENC, str(out)])


def mmss(t):
    t = int(t)
    return f"{t // 60}:{t % 60:02d}"


def cmd_build(list_path, out_path):
    spec = json.loads(Path(list_path).read_text())
    out = Path(out_path)
    tmp = out.parent / (out.stem + "_parts")
    tmp.mkdir(parents=True, exist_ok=True)
    eps = spec["episodes"]
    parts, chapters, t = [], [], 0.0

    def add(p, label=None):
        nonlocal t
        if label:
            chapters.append((t, label))
        parts.append(p)
        t += frames(p) / FPS

    def resolve(f):
        return Path(f) if Path(f).is_absolute() else ROOT / f

    hook = spec.get("hook") or {"file": eps[0]["file"], "start": 0.0, "dur": 4.0}
    p = tmp / "00_hook.mp4"
    episode_part(resolve(hook["file"]), p, hook.get("start", 0.0), hook.get("dur", 4.0))
    add(p, "Intro")
    p = tmp / "01_intro.mp4"
    card(resolve(eps[0]["file"]), p, ["Crayon Babies", spec.get("title", "Fun Songs for Kids!")], 3.0, tmp)
    add(p)
    for i, e in enumerate(eps, 1):
        src = resolve(e["file"])
        c = tmp / f"{i + 1:02d}a_card.mp4"
        card(src, c, [f"Episode {i}", e["title"]], 1.8, tmp)
        add(c, e["title"])
        v = tmp / f"{i + 1:02d}b_episode.mp4"
        episode_part(src, v)
        add(v)
    p = tmp / "99_outro.mp4"
    card(resolve(eps[-1]["file"]), p, ["Bye bye, friends!", "New songs every day!"], 5.0, tmp, subscribe=True)
    add(p, "Bye bye!")

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{x.resolve()}'\n" for x in parts))
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-c:v", "copy", "-af", "aresample=async=1", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
         str(out)])
    # merge too-short chapters (YouTube needs >= 10 s each) into the previous one
    if len(chapters) > 1 and chapters[1][0] - chapters[0][0] < 10:   # short intro -> episode 1 starts at 0:00
        chapters = [(0.0, chapters[1][1])] + chapters[2:]
    merged = []
    for k, (start, label) in enumerate(chapters):
        nxt = chapters[k + 1][0] if k + 1 < len(chapters) else dur(out)
        if merged and (nxt - start) < 10:
            continue
        merged.append((start, label))
    text = "\n".join(f"{mmss(s)} {label}" for s, label in merged)
    out.with_suffix(".chapters.txt").write_text(text + "\n")
    print(f"[compilation] {out} {dur(out):.1f} s, {len(eps)} episodes\n{text}")


def cmd_thumb(video, seconds, words, out, ycenter=0.55):
    """Vertical source: crop a 16:9 band centred at ycenter (0-1 of the height) so the faces are big."""
    tmp = Path(out).with_suffix(".txt")
    tmp.write_text(words)
    wh = run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of",
              "csv=p=0", str(video)]).strip().split(",")
    vw, vh = int(wh[0]), int(wh[1])
    if vh > vw:
        band = int(vw * 9 / 16)
        y = max(0, min(vh - band, int(vh * float(ycenter) - band / 2)))
        base = f"crop={vw}:{band}:0:{y},scale=1280:720:flags=lanczos"
    else:
        base = "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720"
    vf = base + ",eq=saturation=1.15:contrast=1.05," + text_filter(tmp, 150, "h*0.05", bw=14)
    try:
        from PIL import ImageFont
        size = 150
        while size > 70 and ImageFont.truetype(str(FONT), size).getlength(words) > 1180:
            size -= 6
        vf = vf.replace("fontsize=150", f"fontsize={size}")
    except Exception:
        pass
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(seconds), "-i", str(video), "-frames:v", "1",
         "-filter_complex", f"[0:v]{vf}", "-q:v", "3", str(out)])
    print(f"[thumbnail] {out} {Path(out).stat().st_size // 1024} KB")


def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "build":
        cmd_build(sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 6 and sys.argv[1] == "thumb":
        cmd_thumb(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], *(sys.argv[6:7]))
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
