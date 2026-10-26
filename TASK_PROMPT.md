# Crayon Babies — one autopilot run

Everything is in English (titles, descriptions, tags, prompts). No Arabic anywhere.

1. **Credits.** Call ViewMax `get_credits`. One video = 3 shots × 16 = 48 credits.
   If remaining < 48: send a push notification "ViewMax credits low: N left, video skipped", append a
   `skipped: low credits` line to `log/videos.jsonl`, and stop.
2. **Prompts.** Load the skill `crayon-babies-daily-prompt` (Skill tool). If it isn't installed, read
   `skills/crayon-babies-daily-prompt/SKILL.md` in this repo instead. Follow it exactly to pick today's idea and
   write the 3 shot prompts, title, description and tags into `jobs/<date>-<slug>.json`.
3. **Video.** For each shot: ViewMax `generate_video` with model `viewmax-c1`, mode `reference-to-video`,
   `image_urls` = the two character reference URLs below, resolution `768P`, duration `8s`, aspect_ratio `9:16`,
   and an `idempotency_key` like `cb-<date>-<slug>-shotN`. Then `wait_for_task` and collect the mp4 URLs.
   If a shot fails, retry it once with the same key + `-r1`. Do NOT use Veo models: they reject any shot with babies.
   Shot 1 is always a HOOK: something magical bursts out of the paper in the first second, big reaction, short exciting line.
4. **Clips.** Put the 3 mp4 URLs in the job file's `clips` (shot order), plus `viewmax_credits_before`.
5. **Pipeline.** Run `python3 pipeline.py jobs/<file>.json`. It extracts frames, writes a music prompt,
   generates music with Lyria (Gemini API), edits with ffmpeg, uploads as public, madeForKids, synthetic
   media, and logs to `log/videos.jsonl`.
   - Exit 3 = Gemini 402/429: the video was still uploaded without music. Send a push notification
     "Video is up without music - top up $5 for Gemini API on project Video Autopilot" + the link.
   - Any other non-zero exit: send a push notification with the error line.
6. Commit and push `log/` and `jobs/`, then send a push notification with the title + YouTube link.

Character reference images:
- Ava: https://lumilolandkids-lang.github.io/characters/eva.png
- Jimmy: https://lumilolandkids-lang.github.io/characters/jimmy.png
