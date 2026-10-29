# Crayon Babies — weekly Shorts compilation (16:9 long video, every Sunday)

Nobody is watching: never ask questions — decide and continue. Work at extra-high effort on the title, description,
chapters and thumbnail. No ViewMax credits are needed (everything is rebuilt from the week's saved files).
Channel bible: skill `crayon-babies-channel` (or `skills/crayon-babies-channel/SKILL.md`), sections 10 and 11.

## 1. Collect the week
From `log/videos.jsonl` take every entry with `"status": "uploaded"`, kind short (or no kind + a /shorts/ url),
uploaded in the last 7 days (by `time`), oldest first. Each has a job folder `jobs/<date>-<slug>/` (from `job`, or
match the date/slug) with `edit.json`, `song.mp3`, `shots.json`.
- Fewer than 6 shorts with complete job folders → skip: push notification "Compilation skipped: only N shorts this
  week", stop (no commit needed).

## 2. Rebuild each short (free)
For each: `W = runs/compile/<date>-<slug>`; download its Seedance clips from `shots.json` to `W/shotN.mp4`
(`curl -sSL`), copy `song.mp3` and any effect files from the job folder into W, write `W/edit.json` = the saved
edit.json with `"workdir": "<W>"`, then `python3 montage.py build W/edit.json` → `W/final.mp4`.
If a clip URL no longer downloads, leave that short out (say so in the summary).

## 3. Build the compilation
Pick the strongest hook of the week (the most exciting first 3–5 s) for `"hook"`. Write `runs/compile/list.json`
(format in `compile.py` docstring; episode titles = short, friendly versions of the shorts' titles, no emoji), then
`python3 compile.py build runs/compile/list.json runs/compile/compilation.mp4` → also writes
`runs/compile/compilation.chapters.txt`. Check: sample frames at the hook, an episode card, an episode, the outro
(Read the images), duration, loudness printed by ffmpeg.

## 4. Thumbnail
Choose the frame with the biggest, happiest faces + the week's best moment, then
`python3 compile.py thumb <that short's final.mp4> <seconds> "<2-4 WORDS>" ready/<date>-compilation.jpg [ycenter]`.
LOOK at it: faces big and sharp, words readable, nothing cut badly. Adjust seconds/ycenter if needed.

## 5. Publish (Sunday 8:15 AM New York time)
Copy the video to `ready/<date>-compilation.mp4`. Write `jobs/<date>-compilation.json`:
- `title`: e.g. `Crayon Babies Songs for Kids 🎵 | <N> Fun Nursery Rhymes | Week of <Month D>` (section 10 style,
  ≤ 100 characters, hook words first if there is a stand-out song).
- `description`: section 10 template, NO hashtags, with the chapters from compilation.chapters.txt pasted as-is
  (first line must be `0:00 ...`).
- `tags` (start with crayon babies, baby jimmy, baby ava; add kids songs compilation, nursery rhymes for toddlers…),
  `playlist`: "Crayon Babies Songs", `thumbnail`: "ready/<date>-compilation.jpg", `short`: false,
  `publish_at`: Sunday 08:15 New York time in UTC (compute with zoneinfo; if already past, it publishes now).
Run `python3 upload_ready.py jobs/<date>-compilation.json` once (retry once only if it failed before a video id was
printed). Commit and push `log/` and `jobs/<date>-compilation.json`, then remove the mp4/jpg from `ready/` in a
follow-up commit. Push notification: title + link + publish time.

## 6. Finish
Short summary: shorts included, length, title, link, publish time, any short left out and why.
Never print GEMINI_API_KEY / YT_* values. Push only to the `autopilot` branch.
