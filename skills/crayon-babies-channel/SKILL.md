---
name: "crayon-babies-channel"
description: "Use for any work on the Crayon Babies YouTube kids channel: View Max prompts, new episodes, songs, titles, descriptions, tags, thumbnails, editing clips."
---

# Crayon Babies – complete channel bible (updated 5 Nov 2026)

The user runs the YouTube kids channel **Crayon Babies** (@CrayonBabies-TV). She writes in Iraqi/Gulf Arabic; always reply in simple, warm Arabic, short and step-by-step. She sometimes writes Ava's name as "لافا" (Lava) – it means Ava. She makes videos in **View Max** (viewmax.studio – Veo/Kling/Seedance), images in **ChatGPT**, songs in **Gemini**. Every prompt for those tools is in English inside a code block so she can copy it. This file is the single source of truth: never change a character, outfit, room or place description – copy it word for word. When she sends a new image, compare it honestly with these descriptions (hair, eyes, clothes, all three views consistent) before she saves it.

Style: 3D Pixar style, bright soft colors (do not switch to a CoComelon look). Audience: toddlers and preschoolers worldwide, English language. Always Made for kids + AI disclosure = Yes.

The channel is NOT only about crayons: "Crayon Babies" = colorful little kids who draw, play and learn. The Magic Crayon is one series; daily life, outings, doctor, songs and learning are equally welcome. Keep a small colorful touch in every episode (a drawing on the fridge, or the babies drawing today's adventure at the end).

---

## 1. STRICT RULES (every video, no exceptions)

1. **HOOK (0:00–0:03):** shot 1 must stop the scroll. Never start with characters standing, waving, smiling or with an intro. Something magical, surprising, funny or worrying happens in the first second, in close-up, with a big reaction (gasp, wide eyes, giggle). First line is short and exciting ("Oh no!", "Wow! Look!", "What is that?"). Label it `HOOK SHOT – must grab attention in the first second:` and keep it 3 seconds. Good hooks: a drawing bursts out of the paper toward the camera; a giant object pops out bigger than the baby; something funny happens to a baby (rain cloud on Ava's head, puppy licks the face, dinosaur roars); a mystery (shaking glowing box, cracking egg); the problem itself ("Oh no! My toy is broken!"). Long videos and compilations also start with a 3–5 s hook clip before any title card. Thumbnails and short titles reflect the same hook. Reason: the old channel lost 58% of viewers in the first second; the first Crayon Babies short with a magic hook kept 83%.
2. **PROBLEM + SOLUTION:** every video has a clear small problem (lost, broken, sad, scared, mess, mistake, waiting…) and the characters solve it together. The hook teases the problem.
3. **LOOP ENDING:** the last shot visually and verbally returns to the first shot (same place, same object, same framing or line) so the video feels like a circle and replays naturally. Example: starts with the empty paper and "Oh no! The puppy is gone!" → ends with the puppy back on the same paper and "Here you are, puppy!". Label it `LOOP ENDING – mirror shot 1:`.
4. **One lesson / one learning goal** per video, said simply by a character near the end.
5. **Characters always look the same:** copy the exact descriptions below; only outfits may change, and only to one of the listed outfits. For automated clips follow the identity lock in section 13.
6. **Same house, same rooms, same places:** copy the exact location blocks. Never invent another house or another bedroom.
7. **Camera:** medium close-up, faces visible and facing camera, never backs, no far wide shots. Objects appear only AFTER they are drawn/brought. Each character has exactly two arms and two hands. One main action per shot.
8. **Friendly only:** nothing scary, dangerous, violent or gross. Doctors, shots and the dark are gentle and reassuring. No brands, no logos, no famous characters, no look-alikes (never the bald baby that resembles CoComelon's JJ).
9. **Modest clothes for adults:** Mommy, Daddy, Dr. Hana and every adult always wear loose, relaxed, modest, family-friendly clothes – never tight, fitted or curvy. New adult outfits are always written loose (oversized tops covering the hips, wide-leg or straight loose trousers).
10. **Voice lines never a single word** (View Max voice fails on "Cat!"/"Happy!"). Use short phrases ("A little cat!", "I am so happy!"). If View Max offers to change a line, accept the option that keeps a child/adult voice; never accept "stop".
11. **SAVE CREDITS block** in every prompt (below). Tell her to stop View Max with ■ if it regenerates a shot.
12. Always remind her to upload the reference images (section 5 names) of every character and location used – only those that appear in the video.
13. **Every edit uses the approved fast-cut montage style** (section 13, Step 5) unless she asks for something else. **No on-screen words** in the montage (her rule, 29 Oct 2026: "ROAR?", "Meow?!" and similar text looked out of place) – only add text if she asks for it again.
14. **Top quality level, always** (her request, 29 Oct 2026): for everything written for the channel – video and image prompts, song prompts and lyrics, titles, descriptions, tags, edit plans and publishing – use **Claude Opus 5.5** for every chat and scheduled/automated task (her choice, 29 Oct 2026: Fable 5.1 hit the plan's usage limit and costs more – never switch to a pricier model without asking her) and the extra-high effort level: think it through, draft, check every line against this bible (hook, identity keys in CAPS, places word for word, loop ending, one lesson, no hashtags), improve, and only then use it. Never take shortcuts on prompts, songs or publishing.
15. **Every video teaches AND is fun** (her request, 31 Oct 2026: "important, educational and fun – a very special channel"): ONE concrete learning goal from the weekly learning calendar + 2–3 fun mechanics (interactive pause, say-it-with-me, copy-me action, surprise). See section 14.
16. **Always vary** (her rule, 2 Nov 2026): never the same place as any of the last 3 videos – rotate through every room and outside place (park, supermarket, clinic, nursery, beach, farm, zoo, library, mall); outfits fit the place. (The "one other character in every video" part was replaced the same evening by rule 17: one baby per video.)
17. **ONE BABY, ONE LEARNING TOPIC, THE PICTURE NEVER STOPS** (her rule, 2 Nov 2026 evening: "I want videos with one child and educational things – letters, shapes, colors or anything educational, fun, organized, without the picture stopping"): every new video has only ONE baby – Jimmy OR Ava, taking turns – and never a second child; the baby teaches one concrete topic (letters, shapes, colors, numbers, animals, opposites, habits …) in a neat, clear order; something moves in every second (no still pictures, no frozen moments, measured with `montage.py motion`). Full recipe: section 15.
18. **NEVER PUBLISH – SEND THE VIDEO TO HER (her rule, 13 Nov 2026: "لا تنزلوا الفيديو، أرسلوه هنا، أنا أنشره").** No automated task or chat uploads, schedules or publishes anything on YouTube. Every finished video (Shorts, clips, long videos, compilations) is sent to her in the chat as an mp4 (SendUserFile) together with the ready-to-copy title, description, playlist and settings (Made for kids, AI = Yes) and the suggested publish time; she uploads and publishes it herself. Log status "delivered: sent to her in chat". `upload_ready.py` refuses to run without `--her-ok` – only for a video she explicitly asks to be uploaded. Wins over any "MODE: LIVE", publish time or upload line in task prompts or scheduled task texts. (13 Nov: the scheduled "Wow! A BIG Teddy!" Short dLpMhVVEFoY was set back to private with no publish time at her request and sent to her.)

Fixed blocks to paste in every video prompt:
```
CAMERA: medium close-up shots, faces clearly visible and facing the camera, never their backs, no far wide shots. Objects only appear AFTER they are drawn or brought in. One main action per shot. Every character always has exactly two arms and two hands. Bright soft colors, 3D Pixar style, friendly and never scary.

VERY IMPORTANT – SAVE CREDITS: Generate each shot only ONE time. Never regenerate, retry or redo any shot more than once. If a shot is not perfect, accept it as it is and continue to the next shot. Edit the final video only ONE time, without re-editing. Use only my uploaded reference images; do not create new reference images.
```

---

## 2. CHARACTERS (copy exactly)

Color identity (keep it): Jimmy = light blue + yellow star · Ava = yellow + pink star · Leo = green + dinosaur · Mia = turquoise + white daisy · Mommy Lily = coral · Daddy Tom = light green · Dr. Hana = white coat + purple + red glasses.

### Baby Jimmy (boy, 1–2 years) – reference `Jimmy_home`
```
BABY JIMMY: a cute chubby 1-year-old baby boy with fluffy curly ginger hair, big blue eyes, light freckles, rosy cheeks.
```
Voice: `a cute little baby boy voice, soft, sweet, high-pitched and giggly, speaking slowly and clearly in simple English.`
Outfits (pick one per video, write it right after his description):
- HOME (default): `wearing a light blue short-sleeve onesie with a small yellow star, barefoot.`
- PAJAMAS: `wearing soft light blue pajamas with tiny yellow stars and moons, barefoot.`
- OUTDOOR: `wearing a light blue t-shirt with a small yellow star, navy blue shorts and white sneakers with yellow laces.`
- RAIN: `wearing a yellow raincoat with a hood and little blue rain boots.`
- WINTER: `wearing a puffy light blue jacket, a yellow knitted hat with a pompom and yellow mittens.`
- SWIM: `wearing light blue swim shorts with yellow stars and a small orange float ring.`
- PARTY: `wearing a light blue shirt with a tiny yellow bow tie and navy shorts.`
- CHEF: `wearing a tiny white apron with a yellow star and a small white chef hat over his onesie.`
- DOCTOR-PLAY: `wearing a tiny white doctor coat over his onesie with a toy stethoscope.`

### Baby Ava (girl, 1–2 years) – reference `Ava_home`
```
BABY AVA: a cute chubby 1-year-old baby girl with short fluffy curly brown hair, one small curly ponytail on top with a sparkly pink star hair clip, big brown eyes, rosy cheeks.
```
Voice: `a cute little baby girl voice, soft, sweet, high-pitched and cheerful, speaking slowly and clearly in simple English, different from Jimmy's voice.`
Outfits:
- HOME (default): `wearing a soft yellow dress with ruffle sleeves and a small pink flower, and pink baby shoes with bows.`
- PAJAMAS: `wearing soft pink pajamas with tiny yellow stars, barefoot.`
- OUTDOOR: `wearing pink overalls over a yellow t-shirt with a small flower and white sneakers with pink laces.`
- RAIN: `wearing a pink raincoat with a hood and little yellow rain boots.`
- WINTER: `wearing a puffy pink jacket, a yellow knitted hat with a pompom and pink mittens.`
- SWIM: `wearing a pink swimsuit with small yellow flowers and a yellow float ring.`
- PARTY: `wearing a yellow tutu dress with sparkles and pink shoes with bows.`
- CHEF: `wearing a tiny pink apron with a white flower and a small white chef hat over her dress.`
- DOCTOR-PLAY: `wearing a tiny white doctor coat over her dress with a pink toy stethoscope.`
Ava always keeps the sparkly pink star hair clip.

### Mommy Lily – reference `Mommy_home` (loose version, approved)
Her name is **Lily**. The babies call her "Mommy" in dialogue; titles and descriptions may say "Mommy Lily" (e.g. `Cooking with Mommy Lily! 🍪`).
```
MOMMY: a kind young mother in 3D Pixar style, blonde hair in a messy high bun with loose curly strands around her face, big bright blue eyes, rosy cheeks, gentle sweet smile.
```
Outfits (always loose and modest):
- HOME (default): `wearing a loose soft coral oversized short-sleeve t-shirt, light blue wide-leg loose jeans, white sneakers and small gold hoop earrings.`
- OUTDOOR: `wearing a loose soft coral oversized t-shirt, a long beige cardigan, light blue wide-leg loose jeans, white sneakers and a small yellow handbag.`
- KITCHEN: `wearing a loose soft coral oversized t-shirt and light blue wide-leg loose jeans with a mint-green apron.`
- PAJAMAS: `wearing loose soft lilac pajamas.`
- WINTER: `wearing a long cream puffy coat, a coral scarf and light blue wide-leg loose jeans.`
Voice: `a warm, gentle, cheerful young mother's voice, speaking slowly and clearly.`

### Daddy Tom – reference `Daddy_home`
His name is **Tom**. The babies call him "Daddy" in dialogue; titles and descriptions may say "Daddy Tom" (e.g. `Daddy Tom Fixes the Toy! 🔧`).
```
DADDY: a friendly young father in 3D Pixar style, short dark brown curly hair, a short neat dark brown beard, warm brown eyes, thick eyebrows, big happy smile.
```
Outfits (relaxed fit):
- HOME (default): `wearing a soft light green crew-neck sweater, dark blue jeans and white sneakers.` (if a loose re-dressed reference is approved: `dark blue straight-leg loose jeans`)
- OUTDOOR: `wearing a loose light green t-shirt, beige loose chino trousers and white sneakers.`
- KITCHEN: `wearing a light green sweater with a navy blue apron.`
- PAJAMAS: `wearing loose light gray pajamas.`
- WINTER: `wearing a navy puffy jacket, a light green scarf and dark blue jeans.`
Voice: `a warm, playful, friendly young father's voice, speaking slowly and clearly.`

### Dr. Hana (the one family doctor) – reference `DrHana`
```
DR. HANA: a kind, smiling family doctor in 3D Pixar style, a woman with dark brown curly hair in a messy bun, round red glasses, warm brown eyes, rosy cheeks, wearing a long loose white doctor coat with a small red heart pin, a loose light purple top, loose dark gray trousers, white sneakers and a purple stethoscope around her neck.
```
Voice: `a calm, kind, reassuring woman doctor's voice, speaking slowly and clearly.` She explains gently, gives a sticker at the end, never shows needles up close.

### Friends
```
LEO: a cute 2-year-old boy friend with short straight golden blond hair with a little swoop in the front, big green eyes, light skin, rosy cheeks, wearing a green t-shirt with a small dinosaur, beige shorts and green sneakers.
MIA: a cute 2-year-old girl friend with fair rosy skin and very pink cheeks, soft dark curly hair in two round puffs on top of her head tied with turquoise hair bands, big sparkly light honey-amber eyes, wearing a turquoise pinafore dress over a white short-sleeve t-shirt with a small white daisy on the pocket, and white sneakers with turquoise laces.
```
References `Leo`, `Mia`. Voices: Leo `a cheerful little boy voice, speaking slowly and clearly in simple English, different from Jimmy's voice.`; Mia `a sweet little girl voice, speaking slowly and clearly in simple English, different from Ava's voice.`

### Pets and magic friends
```
BISCUIT THE PUPPY (family pet): a fluffy golden puppy with floppy ears, big brown eyes and a red collar with a small gold paw tag; playful, wags his tail and licks faces.
SNOWBALL THE KITTEN: a tiny fluffy white kitten with big blue eyes, pink ears and a pink nose; meows softly.
SUNNY THE LION CUB: a tiny fluffy golden lion cub with a small soft mane tuft on his head, big shiny brown-amber eyes, a cream chest, round paws and a brown tuft on the tip of his tail; cute, round and never scary.
PIP THE LITTLE OWL: a small round fluffy brown owl with huge sparkly amber eyes, a cream face and chest, a small orange beak, tiny wings and orange feet; says "hoo-hoo" and blinks slowly.
ZIGGY THE LITTLE ALIEN: a tiny cute lime-green alien with darker green spots, big shiny green-black eyes, small pointy ears, a cream belly and one curly antenna with a glowing yellow tip; shy and sweet.
THE MAGIC CRAYON: a big chunky crayon that glows and changes color, with tiny sparkles around it.
```
References `Biscuit`, `Snowball`, `Sunny`, `Pip`, `Ziggy`.
New animals/objects for an episode: cute, round, big shiny eyes, never scary, toy-like props; give each a one-line fixed description in a `SUPPORTING CHARACTERS & OBJECTS:` block and reuse it in every shot. Give animals one fitting action/sound (crab walks sideways, monkey makes funny faces). Default from 2 Nov 2026: ONE baby and no other characters (rule 17, section 15); learning objects still get a fixed one-line description. When a new friend becomes recurring, add a named description here.
Names are English on purpose (worldwide English audience; short and easy for toddlers). For a future Arabic version: بسبوس، ثلجة، شموس، بوبو، زيزو.

---

## 3. THE CRAYON HOUSE (one house, fixed rooms – copy exactly)

```
HOUSE OUTSIDE: a cozy two-story pastel yellow house with a blue roof, white windows with flower boxes, a round red front door with a star-shaped window, a small porch with two lanterns, a stone path across green grass, a white picket fence and flower beds.
```
```
LIVING ROOM: a bright cozy living room with cream walls, a big soft mint-green sofa with yellow and pink cushions and a cream knitted blanket, a round light-wood coffee table, a big round rainbow rug, a large window with white curtains on the RIGHT side looking at the garden, three framed family photos on the wall above the sofa (a big photo of the whole family in the middle, Baby Jimmy alone on the left, Baby Ava alone on the right), green plants, a low white bookshelf with picture books and a wicker toy basket.
```
```
KITCHEN: a bright family kitchen with white cabinets and light-wood counters, a pastel yellow fridge covered with children's crayon drawings and fruit magnets, a round white table on a round pastel rainbow rug with two adult chairs, a blue baby high chair and a pink baby high chair, a fruit bowl, a yellow hanging lamp, and a window with small green plants.
```
```
JIMMY'S ROOM: a cozy baby boy's bedroom with light blue walls painted with little yellow stars, yellow curtains, a white toddler bed with a blue star blanket and a yellow star pillow, a rocket-shaped night lamp, a rocket picture on the wall, a blue toy box with yellow stars, a small blue armchair, a round blue rug with a big yellow star, a shelf with toy cars and a soft green dinosaur plush.
```
```
AVA'S ROOM: a sweet baby girl's bedroom with soft pink walls painted with white clouds and little flowers, yellow curtains with flower tie-backs, a white toddler bed with a yellow flower blanket and a small pink star pillow, a butterfly mobile, a pink toy box with white flowers, a soft white bunny plush, a small dollhouse and a fluffy flower-shaped rug.
```
```
PLAYROOM (magic crayon room): a cozy playroom with a colorful puzzle foam floor mat, light blue walls with rainbow pictures, wooden shelves with colorful toy bins, books and toy blocks, a blue bean bag with a yellow star cushion, and a small round wooden table with four little chairs (blue, pink, yellow and green), a big white paper and a box of rainbow crayons on it. Bright, warm, magical lighting with tiny floating sparkles.
```
```
BATHROOM: a bright bathroom with light blue walls and tiles, a round white bathtub with bubbles, a yellow rubber duck, fluffy yellow and pink towels with white flowers, a flower-shaped yellow and pink bath mat, a round wooden mirror, a white sink cabinet with a blue cup with a blue toothbrush and a pink cup with a pink toothbrush, and a small wooden step stool.
```
```
BACKYARD: a sunny backyard with soft green grass, a white fence, a wooden swing hanging on a big apple tree with red apples, a small sandbox with a blue bucket and toys, colorful flower beds, Biscuit's red doghouse with a bone sign and a ball, and the back of the pastel yellow house with the blue roof and a small patio.
```
Magic Crayon episodes start in the PLAYROOM; the crayon turns it into a new world, and the episode returns to the playroom at the end.

## 4. OUTSIDE PLACES (fixed)

Recurring (reference images done): SUNNY PARK, DR. HANA'S CLINIC, LITTLE STARS NURSERY, THE SUPERMARKET. The others appear rarely – View Max draws them from the text; make a reference only if a place starts to repeat.
```
SUNNY PARK: a sunny park with a playground with a red slide and yellow swings, a small duck pond with white ducks and a little wooden bridge, a big green tree, a winding stone path, flower beds and a white bench.
DR. HANA'S CLINIC: a cheerful children's clinic with mint-green walls, a giraffe height chart, a soft blue exam bed with a paper sheet and a small step, framed bunny and elephant pictures, teddy bears, a jar of colorful stickers, a cozy yellow armchair and a big window.
LITTLE STARS NURSERY: a colorful nursery classroom with small round tables and pastel chairs, an alphabet poster, a rainbow rug with a big star, a reading corner with colorful cushions, a play kitchen and a big window.
THE SUPERMARKET: a bright friendly supermarket with wooden crates of colorful fruits and vegetables, neat shelves, green hanging lamps, plants and a small red, yellow and blue kids' shopping cart, no brand names.
THE MALL: a bright, clean shopping mall with a toy store with big windows, an ice cream shop with pastel colors, a small carousel and big green plants.
GRANDMA'S FARM: a small friendly farm with a red barn, a white fence, green fields, a cow, a sheep, hens and a tractor.
THE BEACH: a sunny beach with soft golden sand, gentle blue waves, a striped umbrella and seashells.
THE ZOO: a friendly sunny zoo with green trees and cute round cartoon animals.
THE LIBRARY: a quiet colorful children's library with low bookshelves, bean bags and a story corner.
```
Any new place: describe it in one line with few clear details; add it here if it repeats.

## 5. REFERENCE IMAGES (her photo album "Crayon Babies مراجع")

All character references are **gray-background 3-view sheets** (front, side, back); all places are 16:9 wide images. The image files live in her phone album (they are not inside this skill); upload the matching names to View Max with each prompt. On 26 Oct 2026 she received a zip "Crayon Babies References" with all 24 files already named exactly as in this table (file names = table names + .png for Jimmy_home, Ava_home, Mommy_home, Daddy_home, .jpg for the rest), plus two labeled overview sheets (Characters / Places).

Online copies (public links for automation and image_urls) are on her GitHub Pages site with lowercase names: `https://lumilolandkids-lang.github.io/references/characters/` + jimmy.png · eva.png (Ava) · lily.png · tom.png · leo.jpg · mia.jpg · biscuit.jpg · rory.jpg (= SUNNY the lion cub; old file name, the character is always Sunny) · snowball.jpg · pip.jpg · ziggy.jpg · family.jpg; and `https://lumilolandkids-lang.github.io/references/places/` + house.jpg · living-room.jpg · kitchen.jpg · jimmy-room.jpg · ava-room.jpg · playroom.jpg · bathroom.jpg · backyard.jpg · park.jpg · supermarket.jpg · clinic.jpg · nursery.jpg. When a reference is replaced (e.g. Mia fixed), she uploads it with the same name into the same folder (github.com/lumilolandkids-lang/lumilolandkids-lang.github.io).

| Name | What | Status |
|---|---|---|
| `Jimmy_home` | Jimmy, blue onesie | done |
| `Ava_home` | Ava, yellow dress | done |
| `Mommy_home` | Mommy Lily, loose coral t-shirt + wide-leg jeans | done |
| `Daddy_home` | Daddy Tom, green sweater + jeans | done |
| `DrHana` | Dr. Hana | done (not online yet) |
| `Leo` | Leo, blond, green dino t-shirt | done |
| `Mia` | Mia, turquoise, honey eyes | to fix: back view must show the same curly puffs (no straight pigtails/bows) |
| `Biscuit` `Snowball` `Sunny` `Pip` `Ziggy` | animals | done |
| `House_outside` `Living_room` `Kitchen` `Jimmy_room` `Ava_room` | house | done |
| `Playroom` `Bathroom` `Backyard` | house | done |
| `Sunny_park` `Clinic` `Nursery` `Supermarket` | outside | done |
| `Family` | whole family on the living-room sofa, Biscuit on the rug (poster/thumbnails only) | done |

The single white-background portraits of Jimmy and Ava are for thumbnails and posters only, never video references.
Channel art done: banner 2560×1440 (Jimmy and Ava holding a rainbow crayon, "Crayon Babies" title; content scaled so faces, title and bodies sit inside the central 1546×423 mobile-safe strip; clean sky-and-cloud edges) and profile picture 800×800 (Jimmy and Ava cheek to cheek with the glowing rainbow crayon, no text, white corners filled with sky blue).

Templates:
Re-dress an approved character (upload their reference):
```
Keep this exact same [woman/man/baby]: same face, same hair, same eyes, same smile, same 3D Pixar style. Only change the clothes to: [OUTFIT]. Character reference sheet with front, side and back view, full body, plain light gray background, no text.
```
New character (upload Jimmy and Ava sheets so the style matches):
```
Create a 3D Pixar-style character reference sheet on a plain light gray background, in the exact same 3D style, lighting, colors and baby proportions as the uploaded babies: [PASTE CHARACTER DESCRIPTION + OUTFIT]. Show front view, side view and back view, full body, the same character in all three, soft lighting, no text.
```
Place (upload Jimmy and Ava sheets):
```
Create a 3D Pixar-style wide horizontal 16:9 reference image, in the exact same 3D style, lighting and colors as the uploaded babies: [PASTE LOCATION BLOCK]. Calm, tidy and peaceful, soft warm light, gentle pastel colors. Empty of people, no text.
```
Fix one view of a sheet: `Keep her/him exactly the same in all three views … Fix the [back] view only: …`
When she sends an image to resize: banner → 2560×1440 JPG < 6 MB with key content scaled into the center safe strip and plain sky edges; profile → 800×800 with corners filled with the background color.

---

## 6. CONTENT TYPES & IDEA BANK

### A. Magic Crayon adventures
Done (don't repeat): Rainy Day (butterfly, balloon, rain, umbrella, rainbow) · Magic Crayon (sun, cat, ice cream, dinosaur) · Goodnight Stars (moon, stars, owl, fireflies) · Beach (crab, seashell, sandcastle, wave) · Birthday (balloons, cake, candles, teddy bear) · Lost Puppy (puppy, ball, paw prints) · Space (rocket, moon, alien) · Under the Sea (fish, turtle, octopus, starfish, whale) · Colors Song (2:30).
Done as a music clip (28 Oct 2026, published Short "Baby Lion Can't Roar! 🦁 Never Give Up"): Sunny tries to roar in the BACKYARD and only says "meow"; Jimmy, Ava and Biscuit cheer him on until he ROARS; lesson: never give up. A longer Playroom/magic-crayon story version is still possible later.
Next: Zoo (prompt written) · Snow Day · Farm · Jungle · Castle & friendly dragon · Circus · Train ride · Hot air balloon · Rainbow land · Candy land · Dinosaur valley · Mystery egg series · Friendly Halloween pumpkins (late October) · Christmas · Spring garden.

### B. Good habits & values (problem → lesson)
Patience (waiting for cookies to bake, waiting your turn on the slide) · Cleaning up toys · Washing hands · Brushing teeth · Bath time · Sharing toys · Saying sorry · Please and thank you · Listening to Mommy and Daddy · Healthy food vs junk food · Eating vegetables · Drinking water · Going to bed on time · Potty training · Gentle hands (no hitting) · Being kind to animals · Helping at home · Not wasting food · Being brave · Telling the truth · Good vs bad behavior (show the wrong choice gently, then the right one) · Safety: holding hands crossing the street, not touching the hot stove, staying close in the mall, seatbelt in the car.

### C. Doctor & body (with Dr. Hana)
Check-up visit · Getting a vaccine (brave, gentle) · Having a cold · Tummy ache from too much candy · Boo-boo and bandage · Visiting the dentist · Taking medicine · Why we sleep · Body parts.

### D. Learning
ABC (one letter per short, A–Z series; long video = full alphabet) · Phonics sounds · Numbers 1–10 then 1–20 · Counting objects · Colors · Shapes · Animals and their sounds · Fruits & vegetables · Opposites (big/small, hot/cold) · Feelings (happy, sad, angry, scared) · Days of the week · Weather · Vehicles · Clothes · Rooms of the house · Family members.
Teaching tricks: "Can you guess what I'm drawing?" with a 2 s pause · "Can you say it with me? CAT!" · counting out loud.

### E. Family life & outings
Shopping at the supermarket (healthy choices) · Lost at the mall (stay close) · Picnic in Sunny Park · Playdate with Leo and Mia · First day at Little Stars Nursery · Cooking with Mommy Lily · Fixing a toy with Daddy Tom · Visiting Grandma's Farm · Library story time · Rainy day at home · A friend's birthday.

### F. Songs
Colors song (done) · ABC song · Numbers song · Clean-up song · Brush your teeth song · Wash your hands song (test clip made and edited 26 Oct, approved, not published) · Never give up song (Sunny, done 28 Oct) · Bath song · Healthy food song · Good night song · Animal sounds song · Family song (use the `Family` image) · Doctor song · Feelings song · Days of the week song.

### G. Signature elements
- **Signature series "What's Missing?"** (started 30 Oct 2026, her choice for a unique channel format): the babies' crayon drawing comes to life looking like a REAL toddler's crayon drawing (wobbly thick black outlines, scribbly crayon fill, paper cut-out edge) inside the 3D room – but one part is missing. Ava asks the viewer "What's missing?" (≈2 s pause so kids can shout it), Jimmy draws it, the drawing celebrates; loop back to the paper. Ep. 1 published: "Oh No! Kitty Has No Tail! 🐱 What's Missing?" (PLAYROOM). Next: fish with no tail fin, sun with no rays, car with a missing wheel, giraffe with a short neck, butterfly with one wing, bunny with one ear, house with no door. How: image models refuse "only 3 legs" (they add the 4th) → make the COMPLETE drawing first, then EDIT it to remove the part; all other frames are edits of that hook frame. Keep the incomplete drawing still in motion prompts ("nothing is added to it") – Seedance grows the missing part back if the prompt says the drawing looks at it.
- Catchphrase when the crayon appears: "Magic crayon, draw with me!" with a sparkle chime.
- Closing line: "Bye bye, friends! See you next time!"
- Seasonal episodes in time for searches (Halloween late Oct, winter/Christmas Dec, spring, back to school).

---

## 7. EPISODE STRUCTURE

Long story (60–90 s, 12–18 shots, 16:9):
1. HOOK SHOT (3 s) – the problem or magic moment, close-up.
2. Setup – where we are, who is there.
3. 2–4 discovery/learning moments (one word or idea each).
4. Problem grows.
5. Characters try; Mommy Lily, Daddy Tom, Dr. Hana, a friend or the magic crayon helps.
6. Solution.
7. Lesson in one simple sentence.
8. LOOP ENDING – mirror shot 1.

Short (28–45 s, 6–9 shots, 9:16): hook → problem → solution → loop ending.

Prompt order:
1. Format line · 2. CHARACTERS (+ outfits) · 3. VOICES · 4. SUPPORTING CHARACTERS & OBJECTS · 5. SETTING (location blocks) · 6. CAMERA + SAVE CREDITS · 7. SHOT 1 = HOOK … last SHOT = LOOP ENDING, each with timing, action and one spoken line · 8. `Video only, no text on screen, no background music.`

Formats:
- Long: `Create a [60/75/90]-second HORIZONTAL 16:9 kids' video in 3D Pixar-style animation, made of [12/15/18] shots.`
- Short: `Create a [28/45]-second VERTICAL 9:16 kids' video in 3D Pixar-style animation, made of [6/9] shots.`
- Music video parts: silent (`NO dialogue, NO voices, NO music, NO sound`), 10 shots × 5 s = 50 s per part; song added in editing. Part 1 opens with a hook shot; the last part loops back to the first shot.

---

## 8. SONGS (Gemini) – voices + melody + daf only
The user wants songs with NO musical instruments (her firm rule, for religious reasons) – only children's voices, humming/"la la" melodies, mouth sounds (soft beatbox, clicks), hand claps, finger snaps and a daf. This applies to every song: Shorts, the weekly music video, everything.
```
Create a happy children's nursery song called "[TITLE]".
Style: a cappella children's song. ONLY children's voices singing a simple catchy melody, soft humming and "la la la" harmonies, with a hand drum (daf / frame drum) rhythm and hand claps. NO other instruments: no piano, no guitar, no ukulele, no synth, no strings. Bouncy and joyful, about 110 BPM, major key, very easy for toddlers to sing along.
Vocals (default, one-baby videos – section 15): ONE sweet little boy (Jimmy videos) or ONE sweet little girl (Ava videos) singing solo, high-pitched, slowly and clearly in simple English, with soft children's humming and "la la" backing. (Old two-baby videos: a little boy and a little girl, verses alternate, chorus together.)
Length: about [1:30 / 2:30].
Lyrics:
[Intro – humming + daf]
[Chorus]
[Verse 1]
[Chorus]
[Verse 2]
[Clap break – daf and claps]
[Final chorus]
[Outro – "Bye bye, friends!"]
```
Lyrics rules: short lines, lots of repetition, one learning item per line, sounds/actions ("clap, clap", "splash, splash"), chorus repeated 3–4 times.

---

## 9. PUBLISHING PLAN
**Since 13 Nov 2026 she publishes every video herself (rule 18): the times below are the times SHE should publish at; the automation only makes the video and sends it to her.** (current plan since 5 Nov 2026: 2 long 2:30 learning songs a week + Shorts cut from them + a monthly compilation)
**Current weekly plan (5 Nov 2026):** Friday 3:15 PM NY = new 2:30 school-readiness learning song · Sunday 8:15 AM NY = new 2:30 life-skills/seasonal learning song · the two daily Short slots (6:53 AM and 1:30 PM NY) = 30–45 s clips cut from those two songs (max 2 per song: hook + review/ending, 0 credits) and, in every other slot, a NEW Short made from scratch (~100 credits) – her decision 10 Nov 2026 · last Sunday of the month 7:00 PM NY = compilation of all the month's long songs. Details in the lines below.
Old goal (before 5 Nov 2026, kept for reference only):
- Long 1: a new story episode (Magic Crayon, habits, doctor or outing).
- Long 2: a learning video or a song, or every few days a compilation (5–10 episodes with chapters).
- Short 1 & 2: cut from today's long videos (30–45 s self-contained mini-story starting on the hook, 9:16 with blurred background), or a quick learning short (one letter/number/word).
- Shorts publish at **6:53 AM and 1:30 PM New York time** (she asked for the best time for New York; in Baghdad that is 1:53 PM and 8:30 PM in US summer time, 2:53 PM and 9:30 PM from 1 Nov when New York is UTC-5). Kids' viewing follows school hours: before school, an after-school peak around 3 PM and an evening peak around 7 PM. Upload as private with a scheduled publishAt so there is time to check.
- **FOCUS ON LONG VIDEOS (her rule, 5 Nov 2026: "focus on the long videos – two videos a week"; first "each five minutes", then the same evening "make the song only two and a half minutes"):** every week TWO long 16:9 learning-song videos of about **2:30** each (accept 2:20–2:45) – the most important uploads of the week (long videos bring search, TV and repeat viewing for kids); they get the most care and are never skipped to save credits.
- **Weekly long videos (automated, 16:9):** Friday = a **2:30** school-readiness learning song (Lyria full song first, then 12–16 ViewMax C1 shots of 6–8 s with the chorus shots reused, ≈ 200–250 credits, custom thumbnail), published 3:15 PM New York (11:15 PM Baghdad in winter). Sunday = a NEW **2:30** life-skills/values/seasonal learning song made the same way, published 8:15 AM New York (4:15 PM Baghdad in winter). (The old Sunday Shorts compilation ended on 5 Nov 2026 – there are no new Shorts to compile.)
- **Sunday 8 Nov 2026 = one-time compilation of the 12 rebuildable song Shorts (her request 6 Nov: "on Sunday all the Shorts' songs, clips only, this time")** instead of a new long video, 0 credits; normal Sunday long video again from 15 Nov. Details at the top of TASK_PROMPT_COMPILATION.md.
- **ONE-MONTH TEST (her decision, 6 Nov 2026: "stay on this channel, give it a month; if views don't rise we leave it"):** stay English on this channel, no Arabic channel for now. Baseline 6 Nov: 191 total views, 1 subscriber, 24 videos (Shorts 2–18 views each). Review on **6 Dec 2026**: compare views per long video, total views and subscribers with this baseline; tell her honestly whether it grew. (Option discussed and kept for later: a separate Arabic channel with the same characters – "no instruments" anasheed are a searched niche in Arabic.) YouTube Analytics API is not enabled on project Video Autopilot yet – enabling it would show traffic sources.
- **Why (5 Nov 2026):** after 11 days the channel had 180 views in total, 1–17 per Short and 1 subscriber; kids watch mostly long videos (TV/tablet, search), so she moved the channel's focus to long videos.
- **SHORTS = 2 CLIPS PER LONG VIDEO + NEW SHORTS (her rule 5 Nov 2026 "publish a short clip from the long video", changed 10 Nov 2026 to option B):** a daily Short run first cuts one 30–45 s vertical clip (hook + one item + chorus, `compile.py vclip`, blurred top/bottom, no text) from the newest long video, max 2 clips per long video since 10 Nov 2026 (was 4: too many from the bubble video); every other Short run makes a NEW Short from scratch (old recipe, ~100 credits), 0 credits for clips. Recipe: top of `TASK_PROMPT_MUSIC.md`. The weekly Sunday Shorts compilation is replaced by **long video #2**: a new 2:30 life-skills learning song (Friday = school readiness, Sunday = life skills/values/seasonal), published Sunday 8:15 AM New York. Budget ≈ 2 × 250 = 500 ViewMax credits a week.
- **Monthly "all videos" compilation (her request, 5 Nov 2026):** on the LAST Sunday of each month the Sunday task also rebuilds EVERY long video of the month (Friday + Sunday 2:30 videos, ≈ 20–25 minutes; Shorts are clips of them) into one long 16:9 video, grouped by topic with chapters, a special thumbnail with both babies, published the same Sunday at 7:00 PM New York (0 credits). Recipe: `TASK_PROMPT_COMPILATION.md` step 7.
- (Old, before 5 Nov: Sunday Shorts compilation and new Shorts ≈ 2,000 credits a week – replaced by the rule above); tell her when credits will run out.
- Honest guidance: every upload must be clearly different (new story, new lesson); YouTube can limit channels that mass-upload repetitive AI content. Quality and hooks matter more than quantity; if credits or time are short, 1 long + 2 shorts per day beats rushed videos.

---

## 10. TITLES, DESCRIPTIONS (NO TAGS since 6 Nov 2026)

Strong title formulas (English + emoji, main hook first):
- Hook + character: `Oh No! Baby Ava Lost Her Puppy! 🐶 | Crayon Babies`
- Lesson: `Jimmy Doesn't Want to Share! 🧸 Sharing Is Caring | Good Habits for Kids`
- Question: `What's Inside the Magic Egg? 🥚 | Crayon Babies`
- Learning: `Learn ABC with the Magic Crayon 🖍️ | Alphabet for Toddlers`
- Song: `Clean Up Song 🧹 | Nursery Rhymes & Kids Songs | Crayon Babies`
- Doctor: `Baby Jimmy Gets a Shot 💉 Be Brave! | Doctor Visit for Kids`
- Crayon: `Baby Lion Can't Roar! 🦁 Never Give Up | Crayon Babies`
- Family: `Daddy Tom Fixes the Toy! 🔧 | Crayon Babies`
Shorts: same hook, shorter.

Description template (NO hashtags – she prefers none):
```
[1–2 sentences: hook + what happens, naming the characters]

🎬 What happens in this video:
[3–6 short scene lines with emojis]

📚 Kids learn: [lesson / English words list]

🎶 Voices only: children singing, humming and clapping with a soft hand drum – no other musical instruments.

[Natural keyword sentence: "A fun cartoon for toddlers and preschoolers about …"]

[Keyword line with • : Kids cartoon • Nursery rhymes • Good habits for kids • Learn English for kids • …]

[Chapters if long]

🔔 Subscribe to Crayon Babies for new stories and songs every day!
```
**NO TAGS (her rule, 6 Nov 2026: "remove the tags when you upload the videos"):** upload every video without tags – `upload_ready.py` never sends any (old rule, not used: ~11–15 tags starting with `crayon babies` + the star). Title and description carry the keywords. To remove tags from an uploaded video: videos.update part=snippet with title, description, categoryId and languages but WITHOUT the "tags" field (sending "tags": [] is ignored) – done for _QAYUIUPbIA and tVK9zIZtm9o on 6 Nov.

Upload settings: Made for kids · Altered/synthetic (AI) = Yes · Public · thumbnail 1280×720 JPG < 2 MB · playlists: Magic Crayon Stories / Good Habits / Learn with Crayon Babies / Crayon Babies Songs / Doctor Visits.
Playlists that exist on the channel (4 Nov 2026): "Magic Crayon Stories 🖍️ | Crayon Babies" (PLUFaC4snVLDQ) and "Crayon Babies Songs 🎵 | Sing & Learn for Toddlers" (PLdkGC4jjLl2Q, created 4 Nov with all 13 song Shorts, newest first). `upload_ready.py` matches the job's `playlist` as a case-insensitive part of the title, so `"Crayon Babies Songs"` adds every new Short automatically. Created 6 Nov 2026: "Learn with Crayon Babies 📚 | ABC, Numbers, Shapes & Body Parts for Toddlers" (PLb8lduvPHln0, 12 videos) and "Good Habits for Kids 🦷 | Tidy Up, Brush Teeth, Please & Thank You | Crayon Babies" (PLQn9-7aYAI4M, 8 videos). The job's `playlist` may be a list – every new video goes into "Crayon Babies Songs" + its topic playlist. Doctor Visits does not exist yet.
Channel description rewritten 6 Nov 2026 (learning songs ages 1–5, Jimmy & Ava, "voices only – no piano, guitar or other instruments", new songs Friday and Sunday). Old videos cleaned the same day: hashtags removed (cOyTV_lef6Q, NOZ7_bY9w48), hook-first titles for 3 old videos, audio language "en" everywhere; their old tags were left as they were (the no-tags rule is for uploads).
Growth tracking: `python3 stats.py` → log/stats.jsonl (each Friday/Sunday run); month review on 6 Dec 2026 (section 9).

Thumbnails: designed with **Gemini – Nano Banana 2** (her choice, 29 Oct 2026; 0 credits in the daily pool), never just a cut video frame: big close-up faces with strong emotion, the problem/song object, 2–4 words of huge rounded text (bright yellow, thick purple outline) that match the hook, bright simple background, characters in the exact outfit used. Inputs: 1–2 best approved start frames + the character sheets; identity keys in CAPS; check faces and spelling at full size; fit to 1280×720 JPG < 2 MB. Full recipe: `THUMBNAIL.md` in the repo. First example (29 Oct): "BABY LION ROARS!" – Sunny roaring in the middle, Jimmy and Ava cheering, backyard blurred – approved quality.

---

## 11. EDITING (when she sends clips)
- **Default style for every short = the approved fast-cut montage in section 13, Step 5.**
- Inspect with ffprobe; review frames as a tile grid before commenting. Be honest about flaws (extra hands, objects appearing early, wrong clothes) and fix in editing when possible (cut, slow down, reorder) instead of asking her to spend credits.
- If the opening is weak, move the strongest moment to the start as a hook; make sure the end mirrors the start.
- On-screen words: **off by default** (her rule, 29 Oct 2026). Only if she asks for text again: yellow `0xFFD21F`, purple border `0x5B2A86`, Poppins Bold, pop-in animation; bottom (`y=h*0.83`) for 16:9, top (`y=h*0.11`) for 9:16 (montage.py `"show_words": true`).
- Shorts from long episodes: 1080×1920 with blurred background, hook title at top.
- Songs: subtitle timings from Gemini are approximate; ask her the exact second she hears a line, then shift video and lyrics. Color each color word in its own color.
- Compilations: hook clip → intro card from banner → "Episode N" cards with chime → outro with SUBSCRIBE button (also show it briefly near the start); give chapter timestamps.
- I cannot hear audio; say so instead of claiming a voice sounds good.

## 12. CHANNEL FACTS
- Made-for-kids disables comments, end screens, cards and probably Shorts "Related video"; playlists are the linking tool.
- New channel: views come slowly; judge analytics weekly, not hourly. Key metric: Shorts "Stayed to watch" (first short with a magic hook: 83%; old channel without hooks: 42%).
- Advanced features need a 6-second selfie video verification in Studio (done once).
- Warn her about fake sites (non-Google "Flow" copies) and emails asking for ID or offering sponsorships with downloads.

---

## 14. LEARNING DESIGN – every video teaches, every video is fun (31 Oct 2026)
Audience 1–5 years. A video that is only cute, with nothing a child can learn, copy or answer, is not good enough. Full recipe for the automation: `LEARNING.md` in the repo.

Weekly learning calendar (New York weekday; Short 1 = morning, Short 2 = afternoon):
| Day | Short 1 – school readiness | Short 2 – life skills & values |
|---|---|---|
| Mon | Numbers & counting (1–10 in order, then 1–20) | Healthy habits (wash hands, brush teeth, veggies, water, sleep) |
| Tue | Colors & shapes | Feelings & kindness (sharing, sorry, please/thank you, helping, turns) |
| Wed | Animals & their sounds / nature | Safety (hold hands crossing, hot stove, stay close, seatbelt) |
| Thu | Letters & first words (A–Z in order: letter + sound + 2 words) | Routines & independence (dressing, tidy up, bath, bedtime) |
| Fri | Body parts & opposites | Family & friends (Lily, Tom, Leo, Mia, Biscuit) |
| Sat | "What's Missing?" signature episode | Little science wonder (rain, shadows, seeds, float/sink) |
| Sun | Review song of the week's best word, new story | Seasonal / holiday story |
Series continue in order (next number / letter). The Friday music video is always a full learning song (counting, colors, ABC, animal sounds, body parts, days of the week, clean-up, brushing teeth, feelings).

Fun mechanics (2–3 per video): interactive pause (a character asks the viewer, 1.5–2 s pause with a curious "hmm?" sound, then the answer is celebrated) · say-it-with-me (target word sung ≥ 3 times; the chorus is the lesson) · copy-me action (clap, jump, wave, touch your nose, count fingers) · surprise & payoff (magic crayon reveal, gentle funny mistake, big celebration) · signature touches ("Magic crayon, draw with me!" + sparkle chime, loop ending, "Bye bye, friends!").

Learning checks before spending credits (plan.json → `learning`): goal · 2–4 target words · how the picture shows it · where the words repeat in the lyrics · timestamp of the interactive moment · fact check (numbers, colors, shapes, letters, animal sounds exactly right; objects on screen must match the number sung – ask for the exact number "in a clear row, easy to count" and COUNT them in the frame check) · positive modeling (any wrong choice is gently corrected in the same video) · toddler fit (simple words, bright but calm, nothing scary). Titles and descriptions name the learning goal ("Count to 5 with Jimmy! 🍎 | Learn Numbers | Crayon Babies").

## 15. ONE-BABY LEARNING SHORTS – the default for every new video (her rule, 2 Nov 2026 evening)
Her words: "I want videos with one child and educational things – letters, shapes, colors or anything educational, fun, organized, without the picture stopping."

**Who:** ONE baby per video – Jimmy OR Ava, taking turns video by video (the other baby than the `star` of the last log entry that has one; none yet → Jimmy). Never a second child (no Jimmy + Ava together, no Leo or Mia). By default nobody else is in the picture: the baby and the learning items are the whole story. Only Tue, Wed and Fri afternoon topics (kindness, safety, family) may add ONE grown-up (Mommy Lily / Daddy Tom) or Biscuit – never another child. The baby's voice sings solo.

**What (educational):** one concrete topic from the calendar (LEARNING.md), taught with 2–3 clear items or steps: three colors (red ball, yellow duck, blue cup), three shapes (circle, square, triangle), one letter + its sound + 2 words (A – "a-a" – apple, ant), numbers in order, an animal + its sound, opposites (big/small), healthy-habit steps.
- Letters, numbers and shapes are real 3D objects in the scene (a big chunky foam letter A, wooden shape blocks, plain colored balls) – never overlay text (the no-on-screen-words rule stays).
- Only the target letter/number is visible anywhere in the frame (no posters, books or toys with other letters or numbers – avoid the nursery alphabet poster).
- Colors are pure basic colors, one color per object; counts match the song.
- Check every letter, number, shape, color and count at full resolution (image models mirror letters or add strokes) – wrong → regenerate.

**Organized – the 5 shots:**
1. HOOK – the first item appears by surprise right in front of the baby (pops out of the toy box, rolls in, the Magic Crayon draws it), big gasp, close-up.
2. Item 1: the baby holds / points at / plays with it; the song names it twice.
3. Item 2 – same pattern, same framing.
4. Item 3, or the review: all items in a neat clear row; the baby asks the viewer "Which one is …? Hmm?" (1.5–2 s pause), then the answer is celebrated.
5. LOOP ENDING – mirror of shot 1 (edit of the hook frame), all items neatly in a row, bye-bye wave.
Items come in the same order in the shots and in the song; an item never appears before its shot (story order); each name in the lyrics lands on the cut where that item appears (timestamped lyrics, cut on the word). Calm, uncluttered background: the item is big, centered beside the face and well lit; the place stays recognizable but soft. Places and outfits still rotate (rule 16).

**Camera for one baby:** medium close-up, the baby's face at least a quarter of the frame height, the item beside the face at the same height so both are big; eyes open, facing the camera, exactly two hands.

**The picture never stops:**
- No still images as shots, no zoom on a still, no freeze or hold at the end.
- Every motion prompt keeps the baby AND the item moving for the whole 10 s: the ball bounces, the letter wiggles or spins slowly, the shape slides into place, the baby claps, bounces, points, nods, sways – one clear continuous action, never "small gentle movements" or "holds still".
- Hook slow-down only 0.8–0.9× (the 0.65× hook of "Chocolate on My Teeth" measured 1.2 and looked stopped).
- Final check: `python3 montage.py motion W/final.mp4` – every second must be ≥ 2.0 (median frame difference). Seconds below 2.0 → replace that piece with a livelier moment, raise its speed or cut it shorter, rebuild (free) and measure again. On 2 Nov the slow hook (0 s) and the start of the brushing shot (8–9 s) measured 1.1–1.3 – exactly the moments that look frozen.

**Song:** ONE child voice – a sweet little boy for Jimmy videos, a sweet little girl for Ava videos – singing solo, with soft children's humming / "la la" backing; same a cappella rules (section 8). The song names the items in order, sings the target words ≥ 3 times, has the question + pause, a copy-me line and "Bye bye, friends!".

**Titles:** name the star and the learning goal: `Learn Colors with Baby Ava! 🔴🟡🔵 | Colors for Toddlers | Crayon Babies`, `Letter A with Baby Jimmy! 🍎 | Learn ABC | Crayon Babies`. No tags (her rule, 6 Nov 2026).

**"What's Missing?"** with one baby: the same baby asks the viewer and draws the missing part.

## 13. AUTOMATED MUSIC CLIPS – Seedance 1.0 Pro + start frames (IDENTITY LOCK)

Approved format (26 Oct 2026, "Wash Your Hands Song" test): silent music-clip shots, the Gemini song is added in editing.
- Models in View Max: **Seedance 1.0 Pro** (`seedence-1-0-pro`), image-to-video, 1080p, 10 s, 9:16 → true 1088×1920 at 24 fps, ~2–3 min, **14 credits per shot**, no sound at all. It only offers 5 s or 10 s; always generate **10 s** (a 5 s shot is not cheaper per shot) and make short cuts in editing. **ViewMax C1** is the only cheap model with voices and lip-sync (16 credits / 8 s, 768P) – use it only for talking stories. **Never Veo** (rejects every shot with babies). MiniMax H3 and C1 can sit in the queue for 30+ minutes.
- **Update 1 Nov 2026: Seedance 1.0 Pro was retired by ViewMax.** Automated shots now use **ViewMax C1** image-to-video, 768P, 9:16, 10 s (20 credits per shot, 768×1344, silent prompt "No talking, no dialogue, no music"); identity held well on the first try. All the Seedance rules below (start frames, motion rules, checks) apply the same way.
- Start frames: **Nano Banana 2** image-to-image, 9:16, 2K (0 credits inside her plan's daily pool).

### Step 1 – start frame for every shot
- image_urls: every character sheet in the shot + the place image (online links in section 5). For every shot after shot 1, ALSO add the approved shot-1 frame as an identity anchor.
- Write each character's identity keys in the prompt in CAPS (never rely on the reference images alone):
  - Jimmy: curly GINGER hair, BLUE eyes, FRECKLES, light blue onesie with a yellow STAR.
  - Ava: curly BROWN hair, one small top ponytail, pink STAR clip, BROWN eyes, yellow dress with puffy ruffle sleeves and a small pink flower (no collar, no polka dots).
  - Mommy Lily: golden-blonde messy high bun, BLUE eyes, gold hoop earrings, loose coral oversized t-shirt, light blue wide-leg jeans.
  - Biscuit: fluffy golden puppy, floppy ears, RED collar with a GOLD paw tag.
  - (others: copy their lines from section 2 and capitalise hair color, eye color and signature item)
  - **FACE DESIGN LOCK (her note, 1 Nov 2026: "the face design changed")** – the sheets have a smooth, simple, cartoon-baby face; image models drift to a more realistic, detailed "Pixar" toddler face. Write this in EVERY frame prompt for Jimmy and Ava: `SAME FACE DESIGN AS THE CHARACTER SHEET: VERY BIG ROUND EYES set wide apart (each eye about a quarter of the face width) with LARGE DARK PUPILS, a bright catch-light and THICK DARK UPPER LASHES; a TINY round BUTTON NOSE; a small wide smile with TWO LITTLE TOP TEETH; smooth, soft, simple skin with no skin texture and soft light blush; round wide head; Jimmy only a few faint freckles. Simple stylized cartoon-baby face, not a realistic toddler face.` Smaller eyes, small pupils, missing lashes, a bigger sculpted nose, heavy freckles/blush or detailed skin = wrong face → regenerate. Example of the drift: `assets/face_drift_2026-11-01.jpg` (sheet | wrong frame, Jimmy then Ava).
- Medium close-up: every face large (at least about 1/5 of the frame height), eyes open, faces separate (no cheeks pressed together, no hugs in the start frame).
- **STORY ORDER (her correction, 30 Oct 2026):** nothing that is drawn, made, fixed or brought may be visible before its moment. The "drawing" frame shows the crayon touching the EMPTY spot (nothing drawn yet) and the motion prompt has it drawn line by line following the crayon; never give that frame the finished result.
- **LOOP ENDING frame: never generate from scratch.** EDIT the approved hook frame (image 1 = hook frame): "Keep EVERYTHING in image 1 exactly the same … ONLY CHANGE: …". This keeps identity and framing identical, so the loop is perfect.

### Step 2 – FACE CHECK before spending any credits (mandatory)
Crop every face at full resolution (never judge from a small preview) and tick each identity key: hair color and shape, EYE COLOR, freckles, star/clip, outfit details, place details (e.g. bathroom sink = white cabinet). Any miss → regenerate the frame (free) before animating.

### Step 3 – animate
Seedance 1.0 Pro image-to-video, 1080p, 10 s. The motion prompt repeats the identity keys in CAPS and asks for small, gentle movements with a still camera. Forbidden in the motion: hugging, turning around, covering faces, long closed-eye laughing, someone passing in front of a face – Seedance only sees the first frame, so any face that disappears comes back re-invented. For a big action, use two shots, each from its own checked frame.

### Step 4 – check the clip
Crop the faces at 3 s, 6 s and 9.5 s and compare with the start frame. Also check STORY ORDER on a 4 fps sheet: the drawn/fixed thing is absent before its moment, appears during it, present after (Seedance may add a missing part by itself). If a shot drifted or breaks the order, redo only that shot (14 credits).

### Step 5 – MONTAGE (approved style – use it for every short)
Approved by her on 26 Oct 2026 ("ابغا زي كذا مونتاج دائماً"). Reference edit: `Crayon Babies - Wash Your Hands (test edit).mp4` – 23 s, 8 cuts.
1. **Review first:** make a 1-frame-per-second contact sheet of every 10 s shot. Mark and never use moments with closed eyes, faces looking down or away, blur, identity drift, extra hands, or objects that appear too early.
2. **Cut fast:** from each 10 s shot take its best 1–2 pieces of **2–3.5 s**. A short = 8–10 cuts, about 20–30 s. Hard cuts on action. No extra credits – cutting is free.
3. **Same shot twice → punch-in:** when the next cut comes from the same shot, zoom it ×1.10–1.12 (centred slightly high on the faces) so it feels like a new camera angle, not a jump cut.
4. **Hook:** use only the strongest 1–1.5 s (the gasp/reaction with eyes wide open), slowed to 0.8–0.9× (changed 2 Nov 2026: 0.6–0.65× looked like a stopped picture), and cut away before any blink or look-down.
5. **No on-screen words** (changed 29 Oct 2026 – she found words like "ROAR?" / "Meow?!" out of place). The picture, the song and the sound effects carry the story. (Old style, only if she asks again: one short word per beat, Poppins Bold 130, yellow `0xFFD21F`, purple border `0x5B2A86`, `y=h*0.11`, pop-in 0.25 s.)
6. **Ending:** finish on the loop shot (mirror of the hook), so the replay flows straight back into the hook.
7. **Output:** 1080×1920 (crop 4 px each side from 1088), keep 24 fps, H.264 CRF 17 preset slow, AAC audio (the song, or a silent track if no song), `+faststart`. File name `Crayon Babies - <Title>.mp4`. With a song: song under the whole edit, 1.5 s fade-out, about -14 LUFS.
8. **Final check:** contact sheet of the finished file (look closely at the first 2 s) before sending it to her.

How: `montage.py build edit.json` in the repo does all of this (cuts, speed, punch-in zoom, no text, song, effects, ducking, output settings); `montage.py sheets` and `faces` make the review images.
Getting the clips: the chat workspace cannot reach r2.vibevideo.app; download them in the built-in browser on her laptop into Downloads (fetch → blob → link with `download` name), then copy them over with the device file tools. The Default cloud environment used by the automation can download them directly.

### Step 5b – KID-ATTRACTING VISUAL EFFECTS (her request, 6 Nov 2026)
Every long video and clip (tool: `vfx.py`, called by `montage.py build`):
- `edit.json` → `"bounce": {"amp": 0.03, "ranges": [<every chorus>, <clap break>, <final chorus>]}` – the picture pops a little on each beat
  (vfx.py finds the beats in the song). Not in the verses (calm, the child watches the item).
- `edit.json` → `"vfx"` (6–12 per 2:30 video, never text): a `sparkle` on EVERY moment an item appears / a bubble pops / a
  thing is revealed (x/y = where the item is, read from a frame of final.mp4; `"arc"` so the stars fly AWAY from the face,
  e.g. [20,160] below a nose, [100,260] left of a head), a `sparkle` in the first 0.5 s of the hook, `confetti` on the
  clap break and on the answer "Yay!/There it is!", `hearts` on kindness moments and on "Bye bye, friends!".
- Pair them with library sounds (sfx/sparkle_chime.mp3 vol 0.5 on the hook sparkle, toddlers_cheer_clap.mp3 on the
  answer). Motion prompts ask for big dance moves in chorus shots (bounce, sway, arms up, clap) – faces always visible.
- Setup (fresh cloud container): `python3 -m pip install -q --break-system-packages librosa` and, if `from PIL import Image`
  fails, `python3 -m pip install -q --break-system-packages --ignore-installed --target /usr/local/lib/python3.11/dist-packages pillow`.
  The effects pass takes ~12 min for a 2:30 video (run the build in the background). Confetti has a face keep-out zone
  (`"keep_out": [x, y, rx, ry]`) – set it to where the face is in that cut. Example: jobs/2026-11-06-mv-nose-toes/edit_fx.json.
- LOOK at a 4 fps sheet of each effect moment (no star on the eyes, confetti not hiding the face for long), then
  `montage.py motion` as usual.

### Step 6 – SOUND EFFECTS (approved 28 Oct 2026)
- ViewMax `generate_sound_effect`: **5 credits each**, returns at once (0.5–22 s). Prompt: `<one sound>, cartoon style, cute, kid-friendly, single short sound, clean, no music, no background noise.`, prompt_influence 0.6.
- Per short: 2–4 character moments (no word pops – there are no on-screen words now) (e.g. squeak when Sunny tries to roar, meow, big friendly roar, toddlers cheering). Place each on the exact frame (mouth opens, clap) using a 6 fps contact sheet.
- Mix: effects about as loud as the singing, the song ducked a little under them (sidechain), limiter at about -1.5 dBFS. Measure the levels (I cannot hear).
- Reusable library in the repo `sfx/` (pop, baby_lion_squeak, kitten_meow, lion_cub_roar, toddlers_cheer_clap): reuse for free; only new moments cost credits. Typical short = 70 (5 Seedance shots) + 10–25 (effects) ≈ 80–95 credits.

### Step 7 – SONG LENGTH
- Automation: Lyria `lyria-3-clip-preview` through the Gemini API (Interactions endpoint, prepaid credits on project Video Autopilot, about 8 US cents) is always exactly 30 s; write timestamped lyrics (`[0:00 - 0:03] …`) so lines land on the beats.
- A Gemini-app song longer than wanted (e.g. 35.6 s for a 30 s short): never drop words – cut the leading silence and any gap, speed up with `atempo` (≤ 1.05, not noticeable), trim to the exact length with a 0.8–1.5 s fade-out, loudnorm -14 LUFS.

### Automation tools (repo lumilolandkids-lang/lumilolandkids-lang.github.io, branch `autopilot`)
`TASK_PROMPT_MUSIC.md` (one Short, MODE TEST or LIVE) · `LEARNING.md` (learning calendar + checks) · `TASK_PROMPT_MUSIC_VIDEO.md` (Friday music video) · `TASK_PROMPT_COMPILATION.md` (Sunday compilation) · `compile.py` (compilation, `fit` for Gemini thumbnails) · `THUMBNAIL.md` (Gemini thumbnail recipe) · `montage.py` (contact sheets, face frames, and `build` from an edit.json in exactly this style: cuts, zoom, slow hook, song, effects, ducking, words off by default; 9:16 or 16:9) · `song.py` (Lyria) · `sfx/` library · `upload_ready.py` (uploads a finished mp4: Made for kids, AI = yes, no hashtags, scheduled `publish_at`, optional custom thumbnail) · `assets/Poppins-Bold.ttf`. The Default cloud environment holds the Google keys and can reach Google and r2.vibevideo.app; the chat workspace cannot. Each Short saves its rebuild files (edit.json, song.mp3, shots.json) in `jobs/<date>-<slug>/`; the mp4 is removed from the repo after upload.
Scheduled tasks (all Opus 5.5, Default environment): Daily Short ×2 (runs 4:41 + 8:41 AM New York – since 5 Nov 2026 they cut clips from the long videos), Friday long video (Fri 5:41 AM NY), Sunday long video + monthly compilation (Sun 3:17 AM NY). Texts to paste: below.

### Scheduled task texts (13 Nov 2026 – rule 18: make and SEND to her, never publish)
Daily Short ×2 (4:41 AM + 8:41 AM New York):
```
MODE: DELIVER — make ONE Crayon Babies Short and SEND it to me in the chat. Never upload, schedule or publish anything on YouTube (SKILL.md rule 18). Nobody is watching: never ask questions, decide and continue. Extra-high effort.
1. Clone: git clone --depth 1 -b autopilot https://github.com/lumilolandkids-lang/lumilolandkids-lang.github.io /home/user/autopilot-repo ; git user "Claude" / noreply@anthropic.com ; push only to `autopilot`.
2. Slot: New York time before 07:00 = slot 1 (suggested publish time 6:53 AM NY), otherwise slot 2 (1:30 PM NY).
3. Follow TASK_PROMPT_MUSIC.md and LEARNING.md exactly (Lyria song first – billing error → stop and notify; ~100 ViewMax credits, never Veo; credits < 130 → skip and notify).
4. Channel bible: skills/crayon-babies-channel/SKILL.md (newest). No on-screen words, no hashtags, no tags.
5. Env vars GEMINI_API_KEY, YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN are set – never print them.
6. Deliver: send the mp4 with SendUserFile + the ready-to-copy title, description, playlist, settings (Made for kids, AI = Yes) and suggested publish time. Commit + push log/ and jobs/, push notification "Video ready in the chat: <title>".
```
Friday long video (5:41 AM New York):
```
MODE: DELIVER — make this week's FRIDAY long video and SEND it to me in the chat. Never upload, schedule or publish anything on YouTube (SKILL.md rule 18). Nobody is watching: never ask questions. Extra-high effort.
Clone the repo branch `autopilot` as in the Short task and follow TASK_PROMPT_MUSIC_VIDEO.md: a NEW 2:30 school-readiness learning song (16:9), Lyria song first (billing error → stop and notify), 12–16 ViewMax C1 shots, about 250 ViewMax credits, never Veo, custom thumbnail. Channel bible skills/crayon-babies-channel/SKILL.md. Never print the env keys. Send me the mp4 + thumbnail (SendUserFile) with title, description, chapters, playlist, settings and suggested time (Friday 3:15 PM New York). Commit + push log/ and jobs/ and send a push notification with title and credits used/left.
```
Sunday long video (3:17 AM New York):
```
MODE: DELIVER — make this week's SUNDAY long video and SEND it to me in the chat. Never upload, schedule or publish anything on YouTube (SKILL.md rule 18). Nobody is watching: never ask questions. Extra-high effort.
Clone the repo branch `autopilot` and follow TASK_PROMPT_COMPILATION.md: a NEW 2:30 life-skills / values / seasonal learning song (16:9) made with TASK_PROMPT_MUSIC_VIDEO.md, about 250 ViewMax credits, suggested time Sunday 8:15 AM New York. On the LAST Sunday of the month also build the monthly compilation (step 7, 0 credits, suggested 7:00 PM New York). Channel bible skills/crayon-babies-channel/SKILL.md. Never print the env keys. Send me every mp4 + thumbnail (SendUserFile) with title, description, chapters, playlist and settings. Commit + push log/ and jobs/ and send a push notification.
```
### Lesson learned (2 Nov 2026)
"Oh No! My Tower Fell Down! Count to 5": one C1 clip was unusable (7 wrong-colored blocks) and the run filled the gap with slow zoom-ins on still frames – more than half the video looked frozen and she did not like it. Rule: never use still frames as shots; redo the failed shot once instead (budget allows ~125 credits for this), or recut from the real clips. Motion prompts ask for clear lively action (bounce, clap, point, wiggle), not only "small gentle movements".

### Lesson learned (1 Nov 2026)
"Leaves Fall Down" (backyard, OUTDOOR outfits): she noticed Jimmy and Ava did not look like usual (published anyway). Seen against the sheets: Jimmy's hair darker auburn and flatter instead of bright orange-ginger springy curls, heads/faces rounder and more doll-like, Ava's hair darker and frizzier, warm golden-hour grading shifting skin and hair colors, and both in OUTDOOR outfits while the sheets show the HOME outfits. Cause: the frame check ticked keys from face crops but never put the frame NEXT TO the sheet; frames 2–5 were edited from the hook frame with no character sheets attached, so small drift was copied; the C1 clips were compared only with their own start frame. Fix (every run): (1) put each face crop side by side with the same character's sheet face (montage of the two) and compare hair color/brightness, curl shape, face shape and eye size, not just the key list; (2) attach jimmy.png + eva.png (+ other sheets in the shot) to EVERY frame edit, with "match the character sheets exactly"; (3) prefer the HOME outfits that match the sheets unless the story truly needs another outfit, and then re-check the face against the sheet even harder; (4) ask for "soft even daylight, true colors" instead of golden-hour light; (5) compare the C1 face frames with the sheet too, not only with the start frame.

### Lesson learned (30 Oct 2026)
"What's Missing?" ep. 1: in the drawing shot the kitty's tail was already finished from the first frame, so it looked like the tail appeared before Jimmy drew it (she noticed after publishing). Cause: the drawing start frame was generated with the tail half/fully drawn. Fix: STORY ORDER rule above (empty spot + crayon touching it; drawn line by line in the motion) and a story-order check in Step 4.

### Lesson learned (26 Oct 2026)
In the first test, shot 4 (loop ending) changed the babies: Jimmy got brown eyes and lost his freckles, Ava's hair and dress changed. Cause: its start frame was generated from scratch with smaller faces, a big laughing pose and "cheeks pressed together", with no written identity keys, and it was approved from a small preview; then a hug in the motion hid the faces. Fix that worked: edit the hook frame instead + identity keys in CAPS + full-size face check + hug-free motion. The other 3 shots (playroom hook, bathroom with Mommy Lily, bathroom with Biscuit) kept identity well.
### Lesson learned (2 Nov 2026, "Chocolate on My Teeth")
ViewMax C1 content-rejects image-to-video when an adult's hand touches a toddler in pajamas (Mommy's hand on Jimmy's shoulder) – 4 prompts in a row failed until the frame was edited so nobody touches anybody. Keep adults' hands off the babies in start frames (no touching, not only no hugs). Nano Banana edits also kept copying the toothbrushes from the cups in the hook frame (extra brushes): say "the cups are EMPTY, exactly TWO toothbrushes in the picture" when a prop moves.
### Lesson learned (3 Nov 2026, "Please and Thank You")
ViewMax C1 content-rejected (no charge) 5 motion prompts in the long style ("BABY AVA (…) … she never turns around and nothing passes in front of her face") on close-up frames of Ava; the same frames were accepted with short plain prompts ("3D Pixar style cartoon animation. Still camera. The cartoon girl character with curly BROWN hair, a PINK STAR CLIP and BIG BROWN EYES, wearing her YELLOW DRESS with puffy ruffle sleeves …"). BUT a short prompt that does not name the outfit lets C1 re-dress her (shot 1 came back in a denim jacket and striped shirt) – always name the outfit in CAPS. C1 also often makes its own internal cut (close-up → wide) around 5–6 s and may re-imagine the room (shot 5 turned lilac and wider): read the 1 fps sheet and cut on each half separately.
### Lesson learned (4 Nov 2026, "Hot Hot, Don't Touch!")
ViewMax C1 content-rejected (no charge) every image-to-video prompt for Ava that contained "girl"/"baby girl" or any clothing word ("DRESS", "RUFFLE-SLEEVE OUTFIT", "all in YELLOW") – even on a frame it had accepted on 3 Nov. Find the trigger cheaply with **1 s probe clips (2 credits each)** instead of 10 s tries. What passed: `3D Pixar style cartoon animation. Still camera. … The cartoon character with curly BROWN hair, the PINK STAR CLIP and BIG BROWN EYES <action>. Keep her look exactly as in the picture. Lively movement. Silent.` Without the outfit named, C1 may re-dress her (shot 5 came back in denim overalls): fix = **frames-to-video with the start frame as both first and last frame** – it kept the yellow dress. C1 also mirrored the layout and changed wall colors in some shots; check every clip for a stray second prop at the frame edge and crop it with a punch-in (`montage.py` cut option `"x"`: horizontal crop anchor 0–1, e.g. `"zoom": 1.2, "x": 1.0` cuts the left edge off).
### Lesson learned (5 Nov 2026, "Oh No! What a Mess! Tidy Up")
Nano Banana 2 failed (internal_error) in both 5 Nov runs → nano-banana-2.1 frames (10–12 credits each). ViewMax C1 refused one harmless start frame (Ava sitting, waving) 3× ("cannot be screened" / content_rejected, no charge); a tighter 9:16 crop of the same frame, pushed to the `autopilot` branch and passed as a raw.githubusercontent.com URL, was accepted at once. The same trick gives free extra start frames: grab a good frame from a finished clip (e.g. the empty-rug end state) and animate it – useful when the edit lacks footage of the final state for the answer/lesson lines without breaking story order.
### Lesson learned (6 Nov 2026, "Bubble on My Nose! Body Parts Song" – first Friday 2:30 long video)
Nano Banana 2 internal_error on every call again (frames + thumbnail) → nano-banana-2.1 (hook 2K 12 cr, others 1K 10 cr; thumbnail 10 cr). Image models draw a finger "boop" on the nose as a finger pressed into the side of the nose (looks like nose-picking) – twice; avoid finger-on-nose frames, show the nose with a bubble on it instead. C1 clips of calm "surprise" moments (a bubble resting on nose/ear/tummy/toes) measure 0.2–1.0 motion: `montage.py` now has an optional cut key `"push": [z0, z1]` – a slow push-in/out on a REAL moving clip (never on a still) that lifts those seconds to 2.5–3.5. A 2:30 song needs ~9 C1 clips (≈128 cr) + 8–9 frames; the four choruses reuse s2 (sitting clap), s7 (standing clap) and s9 (dance from a frame grabbed out of s7).
### Lesson learned (13 Nov 2026, "Wow! A Big Red Circle! Shapes Song" – Friday long video)
ViewMax C1 takes "draws a big circle in the air with one finger" literally: it painted thick red circle LINES across Jimmy's face from 1.5 s on (unusable). The redo "moves his raised hand round and round beside the red circle … Nothing is drawn in the air, no lines, no new objects" was clean – always add that line to any "draw in the air / trace" motion. C1 also re-frames freely (wide frames came back zoomed in, close frames pushed in; the loop frame's circle moved to the other side), and wide 4-shape frames (review row, star held up) move very little (motion 1.1–1.9): use them with push-ins at speed 1.3–1.6. Nano Banana 2 worked again (all 12 frames + thumbnail at 0 credits; one "Moderation is unavailable" error, the retry passed). 12 C1 clips × 7 s + 1 redo = 182 credits for a 2:39 video.
### Lesson learned (14 Nov 2026, "Oh No! My Car Can't Go! What's Missing?" #2)
(1) Lyria takes can contain real instruments even with the a cappella prompt: takes 1–2 had synth, bass, xylophone and a drum kit (a "beep beep, vroom vroom" mouth-sound line seemed to push it toward pop production). Cheap check after every song: send the mp3 to Gemini (`gemini-flash-latest` generateContent, inline audio) and ask for JSON `{pitched_instruments, drum_kit, voices_claps_handdrum_only}` – approved older songs came back clean, the bad takes did not; regenerate until clean (8 cents each). The same call gives a timestamped transcription to confirm the answer pause. (2) For "What's Missing?" C1 image-to-video ignored the start frame from 0 s in 2 of 5 shots (re-framed, and DREW THE MISSING WHEEL back) – story order broken. frames-to-video with first = hook frame and last = question frame kept the one-wheel drawing but jumped to another place in the middle (use only its first 0.2 s and last 4 s). Rescue without extra credits: crop the broken clips to the baby only (zoom 1.7–1.9, x 1.0) so the drawing is out of frame. C1 also added real 3D toy wheels to the loop shot – cropped with zoom 1.4, y 0.
