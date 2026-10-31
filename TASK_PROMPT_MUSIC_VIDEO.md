# Crayon Babies — weekly 3-minute MUSIC VIDEO (16:9 long video, every Friday)

Nobody is watching: never ask questions — decide and continue. Work at extra-high effort on the song, every frame
prompt, the edit, title, description and thumbnail (draft → check against the channel bible → improve → use).
Channel bible: `skills/crayon-babies-channel/SKILL.md` in THIS repo (newest; wins over the installed skill) + `LEARNING.md`
(the music video is always a LEARNING SONG with the fun mechanics and learning checks there): sections 1, 2–5 (copy
descriptions word for word), 6F (song list), 8 (song style), 10, 13 (identity lock + montage), plus
`TASK_PROMPT_MUSIC.md` for the exact tool calls (same tools, but 16:9).
Work folder `W = runs/<date>-mv-<slug>`. Budget: at most 230 ViewMax credits (≤ 16 Seedance shots × 14 + effects).

## 1. Credits
`get_credits`. Need ≥ 260, else push notification "Music video skipped: ViewMax credits low (N)" and stop.

## 2. Song first (the video follows the song)
- Topic: the next song from section 6F that is not done and not in `log/videos.jsonl` (or a fitting seasonal one).
  ONE clear learning goal (e.g. brushing teeth steps, counting 1–10, animal sounds), Jimmy + Ava singing,
  at most one extra character/pet, one or two places with reference images.
- Write `W/song_prompt.txt` in the section 8 style (a cappella children's voices, humming/"la la", ONLY daf and
  claps, ~110 BPM, major key, boy + girl voices, verses alternate, chorus together).
  **NO musical instruments at all** (her firm rule, for religious reasons): only children's voices singing, humming and "la la", mouth sounds (soft beatbox, "boom-chk", tongue clicks), hand claps, finger snaps and a daf/frame drum. Write in the prompt: "NO instruments: no piano, no guitar, no ukulele, no bells, no xylophone, no synth, no strings, no flute, no electronic beats".
   with **timestamped sections**
  for a 2:45 song: `[0:00 - 0:06] Hook …`, intro, chorus, verse 1, chorus, verse 2, clap break, final chorus,
  `[2:35 - 2:45] Outro: "Bye bye, friends!"`. Short lines, lots of repetition, one learning item per line.
- `python3 song.py W/song_prompt.txt W/song.mp3 --model lyria-3.5`. Exit 3 (Gemini billing) → stop and notify
  "Music video skipped – top up Gemini API credits"; other errors → read, fix song.py if needed, retry once.
- Measure: duration, where singing starts (silencedetect), and keep the lyric timeline (song.txt + your timestamps).

## 3. Shots (16:9) — identity lock exactly as section 13
Plan 12–16 unique 10 s shots that follow the lyrics: 1 HOOK (first second grabs attention), one shot per verse line
group / learning item, 2–3 CHORUS shots that are REUSED for every chorus (free), and the LOOP ENDING (edit of the
hook frame, "Bye bye!"). Write `W/plan.json`.
- Frames: `nano-banana-2`, aspect_ratio `16:9`, quality `2K`, image_urls = sheets + place (+ hook frame as anchor),
  identity keys in CAPS, faces large and separate, medium close-up. FACE CHECK every frame at full resolution
  before animating (regenerate free, max 3 tries).
- Animate: `seedence-1-0-pro`, image-to-video, `1080p`, `10s`, gentle movements, still camera, no hugs/turning/
  covering faces. Idempotency keys `cb-<date>-mv-<slug>-s<N>`. Download to `W/shotN.mp4`.
- Clip check at 3/6/9.5 s (`montage.py faces`). At most 2 redos in total.

## 4. Edit
`python3 montage.py sheets W`, LOOK at every sheet, then write `W/edit.json` with `"size": [1920, 1080]`:
- Cuts of 2–4 s following the song timeline (cut on the beat/line changes), total = song length minus
  `song_start`. Chorus = the same chorus shots each time but different pieces/zooms so it never looks frozen.
- Hook first (strongest 1–1.5 s, speed 0.6–0.75), end on the loop shot with "Bye bye, friends!".
- **NO on-screen words** (her rule, 29 Oct 2026) — never set `show_words`.
- Effects: optional, at most 4 small ones on clear visual moments. `python3 montage.py build W/edit.json` → LOOK at `final_sheet.jpg` and `final_hook.jpg`; fix and
  rebuild if anything is off.

## 5. Thumbnail — designed with Gemini (Nano Banana 2), see THUMBNAIL.md
Follow `THUMBNAIL.md` → `ready/<date>-mv-<slug>.jpg`.

## 6. Publish (Friday 3:15 PM New York time)
Copy to `ready/<date>-mv-<slug>.mp4`. Write `jobs/<date>-mv-<slug>.json`: title in the song formula
(`<Song Name> <emoji> | Nursery Rhymes & Kids Songs | Crayon Babies`), description per section 10 (NO hashtags; add a
short "Lyrics:" block with the chorus), tags, `playlist` "Crayon Babies Songs", `thumbnail`, `short`: false,
`publish_at` = Friday 15:15 New York in UTC (zoneinfo). Save rebuild files into `jobs/<date>-mv-<slug>/`
(plan, edit, song prompt, song.mp3, shots.json). `python3 upload_ready.py jobs/<date>-mv-<slug>.json` once.
Commit and push `log/` and `jobs/`, then remove the mp4/jpg from `ready/`. Push notification: title + link + time.

## 7. Finish
Summary: song, title, link, publish time, shots made, credits used/remaining, problems and fixes.
Never print GEMINI_API_KEY / YT_* values. Push only to the `autopilot` branch.
