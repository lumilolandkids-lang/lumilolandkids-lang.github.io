# Crayon Babies — weekly 2:30-minute MUSIC VIDEO (16:9 long video, every Friday)

**LONG VIDEOS FIRST (her rule, 5 Nov 2026):** "focus on the long videos – two per week" + (5 Nov, later) "make the song only two and a half minutes".
This Friday video and the Sunday long video are the most important uploads of the week: target length **2:30**
(accept 2:20–2:45), never skip them to save credits for Shorts, and give them the most care (song, shots, thumbnail).
Friday topic = school readiness (numbers, letters, colors & shapes, animals, body parts & opposites); the Sunday long
video (TASK_PROMPT_COMPILATION.md) = life skills & values. **Shorts are now cut from these long videos** (top of
`TASK_PROMPT_MUSIC.md`): plan the song and shots so every 30–45 s part (verse + chorus) works on its own – each verse
starts with a surprising, close-up visual moment (a new item pops in), faces big and centred so a 9:16 crop of the 16:9
frame keeps the baby whole.

Nobody is watching: never ask questions — decide and continue. Work at extra-high effort on the song, every frame
prompt, the edit, title, description and thumbnail (draft → check against the channel bible → improve → use).
Channel bible: `skills/crayon-babies-channel/SKILL.md` in THIS repo (newest; wins over the installed skill) + `LEARNING.md`
(the music video is always a LEARNING SONG with the fun mechanics and learning checks there): sections 1, 2–5 (copy
descriptions word for word), 6F (song list), 8 (song style), 10, 13 (identity lock + montage), plus
`TASK_PROMPT_MUSIC.md` for the exact tool calls (same tools, but 16:9).
Work folder `W = runs/<date>-mv-<slug>`. Budget: at most about 250 ViewMax credits (start frames + 12–16 ViewMax C1 clips + effects).
Models now (Nov 2026): Seedance 1.0 Pro is RETIRED → animate with `viewmax-c1` (image-to-video, `768P`, `16:9`,
2 credits per second – 6–8 s clips, 12–16 credits each). Start frames: `nano-banana-2` (free in the daily pool);
if it returns internal_error twice, use `nano-banana-2.1` (10 credits at 1K, 12 at 2K). Follow the C1 lessons in
SKILL.md section 13 (short plain motion prompts, no clothing words / "girl" for Ava, probe with 1 s clips, re-host a
refused frame as a crop on raw.githubusercontent.com, grab extra start frames from finished clips).

## 1. Credits
`get_credits`. Need ≥ 300, else push notification "Music video skipped: ViewMax credits low (N)" and stop.

## 2. Song first (the video follows the song)
- Topic: the next song from section 6F that is not done and not in `log/videos.jsonl` (or a fitting seasonal one).
  ONE clear learning goal (e.g. brushing teeth steps, counting 1–10, animal sounds), ONE baby singing (bible rule 17 +
  section 15: the other baby than the last log `star`; never a second child, no other characters), one or two places with reference images.
- Write `W/song_prompt.txt` in the section 8 style (a cappella children's voices, humming/"la la", ONLY daf and
  claps, ~110 BPM, major key, ONE child voice matching the star, solo, with soft children's humming backing).
  **NO musical instruments at all** (her firm rule, for religious reasons): only children's voices singing, humming and "la la", mouth sounds (soft beatbox, "boom-chk", tongue clicks), hand claps, finger snaps and a daf/frame drum. Write in the prompt: "NO instruments: no piano, no guitar, no ukulele, no bells, no xylophone, no synth, no strings, no flute, no electronic beats".
   with **timestamped sections**
  for a **2:30 song**: `[0:00 - 0:06] Hook …`, chorus, verse 1, chorus, verse 2, clap break, verse 3 (review of all
  items + the question to the viewer with a 2 s pause), final chorus,
  `[2:20 - 2:30] Outro: "Bye bye, friends!"`. Teach 3–5 items in order (e.g. counting 1–5, 3–4 colors, 3 animals). Short lines, lots of repetition, one learning item per line.
- `python3 song.py W/song_prompt.txt W/song.mp3 --model lyria-3.5` (write "a 2-minute-30-second song" in the prompt). Longer than
  2:45 → trim at a phrase end with a 1.5 s fade (never cut words mid-line); shorter than 2:15 → make it once more. Exit 3 (Gemini billing) → stop and notify
  "Music video skipped – top up Gemini API credits"; other errors → read, fix song.py if needed, retry once.
- Measure: duration, where singing starts (silencedetect), and keep the lyric timeline (song.txt + your timestamps).

## 3. Shots (16:9) — identity lock exactly as section 13
Plan 12–16 unique 6–8 s shots that follow the lyrics: 1 HOOK (first second grabs attention), one shot per verse line
group / learning item, 2–3 CHORUS shots that are REUSED for every chorus (free), and the LOOP ENDING (edit of the
hook frame, "Bye bye!"). Write `W/plan.json`.
- Frames: `nano-banana-2` (fallback `nano-banana-2.1`), aspect_ratio `16:9`, quality `2K`, image_urls = sheets + place (+ hook frame as anchor),
  identity keys in CAPS, faces large and separate, medium close-up. FACE CHECK every frame at full resolution
  before animating (regenerate free, max 3 tries).
- Animate: `viewmax-c1`, image-to-video, `768P`, `16:9`, 6–8 s, LIVELY movements (the picture never stops), still camera, no hugs/turning/
  covering faces. Idempotency keys `cb-<date>-mv-<slug>-s<N>`. Download to `W/shotN.mp4`.
- Clip check at 3/6/9.5 s (`montage.py faces`). At most 2 redos in total.

## 4. Edit
`python3 montage.py sheets W`, LOOK at every sheet, then write `W/edit.json` with `"size": [1920, 1080]`:
- Cuts of 2–4 s following the song timeline (cut on the beat/line changes), total = song length minus
  `song_start`. Chorus = the same chorus shots each time but different pieces/zooms so it never looks frozen.
- Hook first (strongest 1–1.5 s, speed 0.8–0.9), end on the loop shot with "Bye bye, friends!".
- **NO on-screen words** (her rule, 29 Oct 2026) — never set `show_words`.
- **The picture never stops** (her rule, 2 Nov 2026): `python3 montage.py motion W/final.mp4` – every second ≥ 2.0.
- Effects: optional, at most 4 small ones on clear visual moments. `python3 montage.py build W/edit.json` → LOOK at `final_sheet.jpg` and `final_hook.jpg`; fix and
  rebuild if anything is off.

## 5. Thumbnail — designed with Gemini (Nano Banana 2), see THUMBNAIL.md
Follow `THUMBNAIL.md` → `ready/<date>-mv-<slug>.jpg`.

## 6. Publish (Friday 3:15 PM New York time)
Copy to `ready/<date>-mv-<slug>.mp4`. Write `jobs/<date>-mv-<slug>.json`: title in the song formula
(`<Song Name> <emoji> | Nursery Rhymes & Kids Songs | Crayon Babies`), description per section 10 (NO hashtags; add a
short "Lyrics:" block with the chorus), NO tags (her rule, 6 Nov 2026), `playlist` "Crayon Babies Songs", `thumbnail`, `short`: false,
`publish_at` = Friday 15:15 New York in UTC (zoneinfo). Save rebuild files into `jobs/<date>-mv-<slug>/`
(plan, edit, song prompt, song.mp3, shots.json). `python3 upload_ready.py jobs/<date>-mv-<slug>.json` once.
Commit and push `log/` and `jobs/`, then remove the mp4/jpg from `ready/`. Push notification: title + link + time.

**GROWTH CHECKLIST (her request, 6 Nov 2026: "do everything you can so the channel succeeds, don't miss any chance"; one-month test until 6 Dec 2026):**
- `playlist` = a LIST: `["Crayon Babies Songs", "<topic playlist>"]` – topic playlist "Learn with Crayon Babies" (school readiness: letters, numbers, shapes, colors, body parts, animals, nature) or "Good Habits for Kids" (habits, kindness, safety, routines). Clips of a long video go in the same playlists.
- Description: add the line `🎶 Voices only: children singing, humming and clapping with a soft hand drum – no other musical instruments.` right after the "Kids learn" line (honest, and it helps parents who look for music-free songs).
- After the upload: `python3 stats.py` (appends a snapshot to log/stats.jsonl) and put "Channel: N views (191 on 6 Nov), S subscribers; this week's best: …" in the push notification.
- **Month review (the Sunday run on 6 Dec 2026, or the first run after it):** compare log/stats.jsonl with the 6 Nov baseline (191 views, 1 subscriber, 24 videos) and send her an honest push notification: grew or not, best and worst videos, what to try next (the Arabic-channel option is in SKILL.md section 9).

## 7. Finish
Summary: song, title, link, publish time, shots made, credits used/remaining, problems and fixes.
Never print GEMINI_API_KEY / YT_* values. Push only to the `autopilot` branch.
