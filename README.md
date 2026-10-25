# Crayon Babies — Video Autopilot

- `TASK_PROMPT.md` — what the scheduled task does each run (ViewMax → Lyria → ffmpeg → YouTube).
- `pipeline.py` — music, edit, upload, and logging.
- `log/videos.jsonl` — one line per run (title, YouTube link, status, credits used).
- `jobs/` — the job file for each video (idea, shot prompts, clip links).
