# SUNDAY = LONG VIDEO #2 (her rule, 5 Nov 2026) – this replaces the weekly Shorts compilation

Her rules: "focus on the long videos – two a week" (song 2:30) and "don't publish new Shorts, publish short
clips from the long video". So there are no new Shorts to compile any more. Every Sunday: make a NEW 2:30-minute 16:9
LIFE-SKILLS learning song video by following `TASK_PROMPT_MUSIC_VIDEO.md` step by step (song first, 12–16 ViewMax C1
shots, ≈ 200–250 ViewMax credits – credits ARE needed now; skip only if credits < 300), with these differences:
- Topic: Friday = school readiness (numbers, letters, colors & shapes, animals, body parts & opposites); Sunday = life
  skills & values (healthy habits, routines, feelings & kindness, safety, family, little science, or a seasonal/holiday
  song when the date fits). Not a topic or place used in the last 4 long videos. Star = the other baby than Friday's.
- Work folder / job: `<date>-mv-<slug>`, log `"kind": "long"`. Publish Sunday **8:15 AM New York time** (zoneinfo → UTC).
- The weekly steps 1–6 below are OLD (Shorts compilation) and are not used any more; step 7 (monthly) still runs.

---

# Crayon Babies — weekly Shorts compilation (16:9 long video, every Sunday)

Nobody is watching: never ask questions — decide and continue. Work at extra-high effort on the title, description,
chapters and thumbnail. No ViewMax credits are needed (everything is rebuilt from the week's saved files).
Channel bible: `skills/crayon-babies-channel/SKILL.md` in THIS repo (newest), sections 10 and 11.

## 1. Collect the week
From `log/videos.jsonl` take every entry with `"status": "uploaded"`, kind short (or no kind + a /shorts/ url),
uploaded in the last 7 days (by `time`), oldest first. Each has a job folder `jobs/<date>-<slug>/` (from `job`, or
match the date/slug) with `edit.json`, `song.mp3`, `shots.json`.
- **Target length 5:00 (her rule, 5 Nov 2026: two long videos a week, each five minutes; accept 4:40–5:40).** With
  more shorts than needed, pick the strongest and most varied ones (different topics, both babies) to reach ~5:00.
  If the week's shorts are not enough for 4:40, add the best older shorts that were not in last week's compilation.
- Fewer than 6 shorts with complete job folders (this week + older ones) → skip: push notification "Compilation skipped: only N shorts this
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

## 4. Thumbnail — designed with Gemini (Nano Banana 2), see THUMBNAIL.md
Use the week's best moment (its saved start-frame URLs are in the shorts' `shots.json` → `frames`). Follow
`THUMBNAIL.md` → `ready/<date>-compilation.jpg`.

## 5. Publish (Sunday 8:15 AM New York time)
Copy the video to `ready/<date>-compilation.mp4`. Write `jobs/<date>-compilation.json`:
- `title`: e.g. `Crayon Babies Songs for Kids 🎵 | <N> Fun Nursery Rhymes | Week of <Month D>` (section 10 style,
  ≤ 100 characters, hook words first if there is a stand-out song).
- `description`: section 10 template, NO hashtags, with the chapters from compilation.chapters.txt pasted as-is
  (first line must be `0:00 ...`).
- NO tags (her rule, 6 Nov 2026),
  `playlist`: "Crayon Babies Songs", `thumbnail`: "ready/<date>-compilation.jpg", `short`: false,
  `publish_at`: Sunday 08:15 New York time in UTC (compute with zoneinfo; if already past, it publishes now).
Run `python3 upload_ready.py jobs/<date>-compilation.json` once (retry once only if it failed before a video id was
printed). Commit and push `log/` and `jobs/<date>-compilation.json`, then remove the mp4/jpg from `ready/` in a
follow-up commit. Push notification: title + link + publish time.

## 6. Finish
Short summary: shorts included, length, title, link, publish time, any short left out and why.
Never print GEMINI_API_KEY / YT_* values. Push only to the `autopilot` branch.

## 7. MONTHLY "ALL VIDEOS" COMPILATION (her request, 5 Nov 2026: "and at the end of the month, all the videos together")
Run this ONLY on the LAST Sunday of the month (New York date: next Sunday falls in the next month), AFTER that
Sunday's new long video is uploaded. 0 ViewMax credits.
- Collect every LONG video of this calendar month from `log/videos.jsonl` (the Friday and Sunday 2:30 videos,
  `jobs/<date>-mv-<slug>/`), oldest first – about 8–10 videos, ≈ 20–25 minutes. (Shorts are clips of these, so they
  are not added again; older Shorts made before 5 Nov may be added at the end of the October/November video only.)
  Rebuild each one from its job folder exactly as in step 2 (music videos: their edit.json has `"size": [1920, 1080]`).
  A clip that no longer downloads → leave that video out and say so.
- Order: hook (the month's strongest 4–5 s) → intro card "This Month's Songs!" → the videos grouped by topic
  (songs/music videos first as anchors, then letters, numbers, colors & shapes, animals, habits & safety, feelings &
  family, science, seasonal), each with its "Episode N" card → SUBSCRIBE outro. Also show the SUBSCRIBE reminder
  briefly near the start (section 11). Write `runs/compile/month-list.json` and run
  `python3 compile.py build runs/compile/month-list.json runs/compile/month.mp4` (long run: rebuild clips one by one).
  Check samples (hook, cards, a short, a music video, outro), duration and loudness.
- Thumbnail (THUMBNAIL.md): BOTH babies' best happy faces from the month (each from their own approved start frame,
  side by side, never touching), the month's best objects, 2–4 huge words, e.g. "1 MONTH OF SONGS!".
- Publish the SAME Sunday at **7:00 PM New York time** (the evening kids' peak): `jobs/<date>-month.json` with
  title e.g. `Crayon Babies – All <Month> Songs! 🎵 <N> Learning Songs for Toddlers | <M> Minutes`
  (≤ 100 characters), description per section 10 (NO hashtags) with the chapters pasted as-is and a "📚 This month kids
  learned:" line listing the learning goals, NO tags (her rule, 6 Nov 2026) (old list, not used: crayon babies, baby jimmy, baby ava, kids songs compilation,
  nursery rhymes for toddlers, learning songs for toddlers …), playlist "Crayon Babies Songs", thumbnail, `short`: false.
  Upload once, log it with `"kind": "monthly"`, commit + push `log/` and `jobs/`, remove the mp4/jpg from `ready/`,
  push notification: title + link + publish time + length.
