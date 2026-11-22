#!/usr/bin/env bash
# Rebuild the final 16:9 video of "Wow! A Little Pumpkin! Count to 5" (2:29) from the saved files -> ready/2026-11-20-mv-count-pumpkins.mp4
# Run from the repo root: bash jobs/2026-11-20-mv-count-pumpkins/rebuild.sh   (~15 min, 0 credits)
set -euo pipefail
J=jobs/2026-11-20-mv-count-pumpkins
W=runs/2026-11-20-mv-count-pumpkins
mkdir -p "$W" ready
python3 -c "import librosa" 2>/dev/null || python3 -m pip install -q --break-system-packages librosa
python3 -c "from PIL import Image" 2>/dev/null || python3 -m pip install -q --break-system-packages --ignore-installed --target /usr/local/lib/python3.11/dist-packages pillow
for n in 1 3 4 5 6 7 9 10 11 12; do
  url=$(python3 -c "import json;print(json.load(open('$J/shots.json'))['shot$n'])")
  [ -s "$W/shot$n.mp4" ] || curl -sSL --retry 4 -o "$W/shot$n.mp4" "$url"
done
cp "$J/song.mp3" "$W/song.mp3"
python3 montage.py build "$J/edit.json"
python3 montage.py motion "$W/final.mp4" | tail -1
cp "$W/final.mp4" ready/2026-11-20-mv-count-pumpkins.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 ready/2026-11-20-mv-count-pumpkins.mp4
