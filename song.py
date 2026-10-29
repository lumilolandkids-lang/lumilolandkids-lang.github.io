#!/usr/bin/env python3
"""Make a Crayon Babies song with Lyria (Gemini API, Interactions endpoint) and save it as MP3.

Usage: python3 song.py PROMPT.txt OUT.mp3 [--model lyria-3-clip-preview|lyria-3.5]

- lyria-3-clip-preview (default): always exactly 30 s - perfect for Shorts.
- lyria-3.5: full songs (length steered in the prompt, e.g. "a 2-minute song" or timestamped sections).
The prompt holds the musical direction AND the lyrics with section tags ([Verse], [Chorus]) or timestamps
([0:00 - 0:04] ...). Lyrics/structure text returned by Lyria is saved next to the MP3 as OUT.txt.

Exit codes: 0 ok, 2 bad input, 3 Gemini billing/quota (HTTP 402/429 - top up prepaid credits), 4 other error.
Never prints the API key.
"""
import base64, json, os, subprocess, sys, time, urllib.error, urllib.request
from pathlib import Path

API = "https://generativelanguage.googleapis.com/v1beta/interactions"


def call(url, data=None, method=None):
    key = os.environ.get("GEMINI_API_KEY", "")
    if not key:
        raise SystemExit("GEMINI_API_KEY is not set")
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method or ("POST" if body else "GET"),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, {"raw": raw[:500].decode(errors="replace")}


def blocks(resp):
    """Yield every content block of the model output (handles a few response shapes)."""
    for step in resp.get("steps", []) or []:
        if step.get("type") in ("model_output", None):
            for b in step.get("content", []) or []:
                yield b
    for k in ("outputs", "output"):
        for b in resp.get(k, []) or []:
            if isinstance(b, dict):
                yield b
    if isinstance(resp.get("output_audio"), dict):
        yield {"type": "audio", **resp["output_audio"]}
    if isinstance(resp.get("output_text"), str):
        yield {"type": "text", "text": resp["output_text"]}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    prompt = Path(sys.argv[1]).read_text().strip()
    out = Path(sys.argv[2])
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "lyria-3-clip-preview"
    code, resp = call(API, {"model": model, "input": prompt})
    if code in (402, 429):
        print(f"GEMINI BILLING/QUOTA ERROR HTTP {code}: {json.dumps(resp)[:400]}")
        return 3
    if code not in (200, 201):
        print(f"ERROR HTTP {code}: {json.dumps(resp)[:600]}")
        return 4
    # Long-running interactions: poll until the audio is there.
    waited = 0
    while not any(b.get("type") == "audio" and b.get("data") for b in blocks(resp)):
        status = str(resp.get("status", "")).lower()
        if status in ("failed", "cancelled", "error") or waited > 600 or not resp.get("id"):
            print(f"ERROR no audio (status={status!r}): {json.dumps(resp)[:600]}")
            return 4
        time.sleep(10)
        waited += 10
        code, resp = call(f"{API}/{resp['id']}")
        if code != 200:
            print(f"ERROR polling HTTP {code}: {json.dumps(resp)[:400]}")
            return 4
    audio = next(b for b in blocks(resp) if b.get("type") == "audio" and b.get("data"))
    out.write_bytes(base64.b64decode(audio["data"]))
    text = "\n".join(b.get("text", "") for b in blocks(resp) if b.get("type") == "text").strip()
    if text:
        out.with_suffix(".txt").write_text(text)
        print("[lyrics/structure]\n" + text[:2000])
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)],
                         capture_output=True, text=True).stdout.strip()
    vol = subprocess.run(["ffmpeg", "-nostdin", "-i", str(out), "-af", "volumedetect", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    mean = [l.split(":")[-1].strip() for l in vol.splitlines() if "mean_volume" in l]
    print(f"[song] {out} model={model} duration={dur}s mean_volume={mean[0] if mean else '?'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
