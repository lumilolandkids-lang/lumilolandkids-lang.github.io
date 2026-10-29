#!/usr/bin/env python3
"""Crayon Babies montage tool - the approved fast-cut style (channel bible, section 13, Step 5).

Commands
  python3 montage.py sheets W               contact sheet per shot: W/sheets/shotN.jpg (1 frame per second, timestamps)
  python3 montage.py faces W N T [T ...]    full-resolution frames of W/shotN.mp4 at times T: W/check/shotN_T.jpg
  python3 montage.py build EDIT.json        build the final video, then W/final_sheet.jpg + W/final_hook.jpg

W is a work folder holding shot1.mp4 ... shotN.mp4 (Seedance 1088x1920, 24 fps, 10 s, silent).

EDIT.json
{
  "workdir": "runs/2026-10-30-bubbles",          # W (relative to this repo or absolute)
  "out": "final.mp4",                             # written inside W
  "song": "song.mp3",                             # inside W, or null for a silent track
  "song_start": 0.0,                              # seconds to skip at the start of the song (leading silence)
  "cuts": [                                       # in order; output length of a cut = dur / speed
    {"shot": 1, "start": 0.0, "dur": 1.2, "speed": 0.6, "word": "Oh no!"},   # hook: slowed, word from the start
    {"shot": 1, "start": 3.0, "dur": 2.0, "zoom": 1.10},                     # same shot again -> punch-in
    {"shot": 2, "start": 0.4, "dur": 2.6, "word": "Can I try?"}
  ],
  "sfx": [                                        # "cut" = index in cuts, "offset" = seconds after that cut starts
    {"file": "sfx/squeak.mp3", "cut": 0, "offset": 0.05, "vol": 0.55, "max": 1.0}
  ],
  "pop_on_words": true                            # adds sfx/pop.mp3 when each word appears
}
sfx paths are looked up in W first, then in this repo. "max" (optional) trims the effect to that many seconds.
Words: Poppins Bold, yellow 0xFFD21F, purple border 0x5B2A86, at y=h*0.11, pop-in 0.25 s, from 0.12 s into the cut.
Audio: song trimmed to the video length with a 1.5 s fade-out, effects mixed on top and the song ducked
slightly under them, limited to about -1.5 dBFS. Output: 1080x1920, 24 fps, H.264 CRF 17, AAC 192k, +faststart.
"""
import json, math, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONT = ROOT / "assets" / "Poppins-Bold.ttf"
FPS = 24
TEXT_DELAY = 0.12
POP = "sfx/pop.mp3"


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.stderr.write(p.stderr[-3000:])
        raise SystemExit(f"ffmpeg failed: {' '.join(map(str, cmd))[:300]}")
    return p.stdout


def ffprobe_duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]))


def wpath(w):
    w = Path(w)
    return w if w.is_absolute() else (ROOT / w)


def font_size(text, max_size=130, max_width=980):
    try:
        from PIL import ImageFont
        size = max_size
        while size > 60:
            f = ImageFont.truetype(str(FONT), size)
            if f.getlength(text) + 20 <= max_width:
                return size
            size -= 4
        return size
    except Exception:
        return max(60, min(max_size, int(max_width / (0.62 * max(len(text), 1)))))


def tile(src, out, vf_pre, cols, rows, width=270):
    label = (f"drawtext=fontfile={FONT}:text='%{{pts\\:hms}}':fontsize=22:fontcolor=white:"
             f"box=1:boxcolor=black@0.6:x=4:y=4")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(src), "-vf",
         f"{vf_pre},scale={width}:-1,{label},tile={cols}x{rows}", "-frames:v", "1", str(out)])


def cmd_sheets(w):
    w = wpath(w)
    (w / "sheets").mkdir(exist_ok=True)
    for shot in sorted(w.glob("shot*.mp4")):
        out = w / "sheets" / (shot.stem + ".jpg")
        tile(shot, out, "fps=1", 10, 1)
        print(out)


def cmd_faces(w, n, times):
    w = wpath(w)
    (w / "check").mkdir(exist_ok=True)
    for t in times:
        out = w / "check" / f"shot{n}_{t}.jpg"
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t), "-i", str(w / f"shot{n}.mp4"),
             "-frames:v", "1", "-q:v", "2", str(out)])
        print(out)


def find_file(w, rel):
    for base in (w, ROOT):
        p = base / rel
        if p.exists():
            return p
    raise SystemExit(f"file not found: {rel}")


def build_cut(w, i, c, seg_dir):
    speed = float(c.get("speed", 1.0))
    zoom = float(c.get("zoom", 1.0))
    frames = max(1, round(float(c["dur"]) / speed * FPS))
    vf = []
    if speed != 1.0:
        vf.append(f"setpts=PTS/{speed}")
    vf.append(f"scale=trunc(1088*{zoom}/2)*2:trunc(1920*{zoom}/2)*2:flags=lanczos")
    vf.append("crop=1080:1920:(iw-1080)/2:(ih-1920)/2*0.85")
    vf.append(f"setsar=1,fps={FPS},format=yuv420p")
    word = (c.get("word") or "").strip()
    if word:
        txt = seg_dir / f"{i:02d}.txt"
        txt.write_text(word)
        s = font_size(word)
        vf.append(
            f"drawtext=fontfile={FONT}:textfile={txt}:fontcolor=0xFFD21F:borderw=10:bordercolor=0x5B2A86:"
            f"fontsize='if(lt(t-{TEXT_DELAY},0.25),40+{s - 40}*max(t-{TEXT_DELAY},0)/0.25,{s})':"
            f"x=(w-text_w)/2:y=h*0.11-text_h/2:enable='gte(t,{TEXT_DELAY})'")
    out = seg_dir / f"{i:02d}.mp4"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(c["start"]), "-t", str(float(c["dur"]) + 0.5),
         "-i", str(w / f"shot{c['shot']}.mp4"), "-vf", ",".join(vf), "-frames:v", str(frames), "-an",
         "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-r", str(FPS), str(out)])
    got = int(run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v",
                   "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(out)]).strip())
    return out, got


def cmd_build(edit_path):
    edit = json.loads(Path(edit_path).read_text())
    w = wpath(edit["workdir"])
    seg_dir = w / "segments"
    shutil.rmtree(seg_dir, ignore_errors=True)
    seg_dir.mkdir(parents=True)
    cuts = edit["cuts"]

    # 1. video cuts
    starts, t_frames, lst = [], 0, []
    for i, c in enumerate(cuts):
        out, n = build_cut(w, i, c, seg_dir)
        starts.append(t_frames / FPS)
        t_frames += n
        lst.append(f"file '{out}'")
    total = t_frames / FPS
    (seg_dir / "list.txt").write_text("\n".join(lst) + "\n")
    video = seg_dir / "video_only.mp4"
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(seg_dir / "list.txt"),
         "-c", "copy", str(video)])
    print(f"[video] {len(cuts)} cuts, {total:.2f} s")
    for i, (c, s) in enumerate(zip(cuts, starts)):
        print(f"  cut {i:2d} @ {s:6.2f}s  shot{c['shot']} {c['start']}+{c['dur']}s  {c.get('word') or ''}")

    # 2. effects bus
    fx = list(edit.get("sfx", []))
    if edit.get("pop_on_words", True):
        fx += [{"file": POP, "cut": i, "offset": TEXT_DELAY, "vol": 0.45, "max": 0.2}
               for i, c in enumerate(cuts) if (c.get("word") or "").strip()]
    fx_wav = seg_dir / "fx.wav"
    if fx:
        ins, parts, labels = [], [], []
        for k, e in enumerate(fx):
            at = starts[int(e["cut"])] + float(e.get("offset", 0))
            ins += ["-i", str(find_file(w, e["file"]))]
            trim = f",atrim=0:{float(e['max'])},afade=t=out:st={max(float(e['max']) - 0.12, 0)}:d=0.12" if e.get("max") else ""
            parts.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo{trim},"
                         f"volume={float(e.get('vol', 0.6))},adelay={int(round(at * 1000))}:all=1[e{k}]")
            labels.append(f"[e{k}]")
        fc = ";".join(parts) + ";" + "".join(labels) + f"amix=inputs={len(fx)}:normalize=0:duration=longest[fx]"
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[fx]",
             "-ar", "48000", "-c:a", "pcm_f32le", str(fx_wav)])
    else:
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
             "-t", "1", "-c:a", "pcm_f32le", str(fx_wav)])

    # 3. song (trimmed, faded, -14 LUFS) + ducking under the effects + limiter
    mix = seg_dir / "mix.wav"
    if edit.get("song"):
        song = find_file(w, edit["song"])
        ss = float(edit.get("song_start", 0))
        fade = max(total - 1.5, 0)
        fc = (f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim={ss}:{ss + total},asetpts=PTS-STARTPTS,"
              f"apad,atrim=0:{total},afade=t=out:st={fade:.3f}:d=1.5,loudnorm=I=-14:TP=-1.5:LRA=11,"
              f"aresample=48000[song];[1:a]apad,atrim=0:{total},asplit=2[k][m];"
              f"[song][k]sidechaincompress=threshold=0.06:ratio=3:attack=8:release=280[duck];"
              f"[duck][m]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.84:attack=3:release=60:level=disabled[out]")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(song), "-i", str(fx_wav), "-filter_complex", fc,
             "-map", "[out]", "-t", f"{total:.3f}", "-ar", "48000", str(mix)])
    else:
        fc = (f"[0:a]apad,atrim=0:{total},alimiter=limit=0.84:level=disabled[out]")
        run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(fx_wav), "-filter_complex", fc,
             "-map", "[out]", "-t", f"{total:.3f}", "-ar", "48000", str(mix)])

    # 4. mux
    out = w / edit.get("out", "final.mp4")
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(video), "-i", str(mix), "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", str(out)])

    # 5. checks
    tile(out, w / "final_sheet.jpg", "fps=1", 10, math.ceil(total / 10))
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-t", "2.75", "-i", str(out), "-vf",
         f"fps=4,scale=200:-1,tile=11x1", "-frames:v", "1", str(w / "final_hook.jpg")])
    p = subprocess.run(["ffmpeg", "-nostdin", "-i", str(out), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    summary = [l.strip() for l in p.stderr.splitlines() if l.strip().startswith(("I:", "Peak:"))][-2:]
    print(f"[final] {out}  {ffprobe_duration(out):.2f} s  {' | '.join(summary)}")
    print(f"[check] look at {w / 'final_sheet.jpg'} and {w / 'final_hook.jpg'}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    if cmd == "sheets":
        cmd_sheets(sys.argv[2])
    elif cmd == "faces":
        cmd_faces(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif cmd == "build":
        cmd_build(sys.argv[2])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
