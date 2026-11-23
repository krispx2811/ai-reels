---
name: ai-reels
description: Catalogue of 15 short-form vertical video formats (Reels / TikTok / Shorts) and 14 visual styles (Gulf heritage, claymation, papercraft, neon night, Apple-keynote product, clay diorama, toon outlines, flat vector, isometric, pixel art, sketch, risograph, vinyl toy, kinetic 3D type): 7 story formats studied from real viral reels and 8 3D showcase formats from the threejs.org gallery (product hero, tiny world diorama, 3D kinetic type, particle globe, satisfying physics, chase cam, glass/liquid, cozy room), with how to build each one locally in Blender or three.js for free (HyperFrames, three.js, Blender + Kenney CC0 kits, ElevenLabs voice), without AI video models. Use when the user wants a reel, short, TikTok, story ad, POV video, "what if" video, choose-your-path / "comment A or B" video, Roblox-style story, motion comic, or cartoon explainer, or asks "what kinds of videos can you make", or shares an Instagram/TikTok reel as a style reference.
---

# AI Reels

Fifteen formats: 7 story formats taken apart from real viral reels (`references/formats.md`) and 8 3D
showcase formats from the threejs.org gallery (`references/threejs-formats.md`).
Pick ONE format per video (a story can cut to one showcase shot), then follow its recipe. Every format shares the same spine:

1. **Hook in the first 1.5 s**: a question or a shock line in 2nd person ("What if you...", "Your bank just sent you...").
2. **Rehook at about 40%**: a twist, a countdown, a new chapter card, or a phone buzz.
3. **Payoff**, then an **end card**: a choice ("Comment A or B, the majority writes Part 2"), a CTA, or a logo.
4. Vertical 1080 x 1920, 30 fps. Words on screen are short and timed to speech.

## The formats (pick one)

| # | Format | Looks like | Best for | Build with |
|---|---|---|---|---|
| 1 | **Toon POV story** | Cel-shaded 3D game world, black ink outlines, first-person with your hands in frame, chapter cards "DAY 1 / place" | Survival-style stories, "a day in the life of a shop owner", product shown in your hands | Blender (GPU, EEVEE + toon + Line Art) or three.js toon in HyperFrames; Kenney CC0 kits |
| 2 | **"What if" life sim** | Semi-real 3D people (game engine), 2nd-person narration, HUD counters (AGE 24 / LIVED 30 YEARS / PAUSE), typewriter mono subtitles | Big-idea hypotheticals, philosophy, "would you press it?" | Blender or three.js scenes + HTML HUD overlay |
| 3 | **Illustrated "You decide" thriller** | Painted 2D illustration stills with slow push-ins, phone UI inserts (bank app, texts, news), HUD bar (balance, time left), bold caps captions with key words in yellow/red, "REAL STORY" tags | Money / scam / news dilemmas, fintech, apps | Still illustrations + HyperFrames (Ken Burns, UI mock-ups in HTML) |
| 4 | **Flat vector motion comic** | Flat 2D vector characters, dark palette, clock stamp top-left ("3:00 AM"), series tag top-right, phone text messages full screen, stat HUD (WATER / FOOD / HOURS LEFT), countdown | Tense POV stories, survival, jobs, any "you have X minutes" | SVG/canvas drawn in HyperFrames (fully code-made) |
| 5 | **Cinematic toy-figure 3D** | Vinyl/clay toy characters, soft cinematic light and depth of field, dark interiors to bright outdoors, poll comments from the last part popping on screen, choice buttons placed over the scene | Serialized story with audience votes ("Part 4") | Blender (EEVEE, DOF, bloom off), simple figure rigs |
| 6 | **Roblox-style narrated story** | Blocky avatars, bright toy worlds, ONE WORD AT A TIME big captions (yellow/white, black stroke) synced to the narrator, a cut every 1 to 2 s | Kids/teen stories, rules-based mysteries ("only comes at midnight") | three.js or Blender with blocky Kenney/self-made characters + word-timed captions |
| 7 | **Cartoon dialogue explainer** | Flat 2D characters face to face, speech bubbles, fixed title header ("What to do when..."), LEVEL meter with âœ— wrong / âœ“ right rules, stamp labels ("WENT COLD"), level-up structure, brand CTA at the end | Teaching a skill, objections handling, "do / don't" for a product | SVG characters + HTML bubbles in HyperFrames |

Full breakdowns (timing, type, colours, overlays, end cards, what to copy and what to avoid) are in
`references/formats.md`. Read the section for the chosen format before writing anything.

### 3D showcase formats (from the threejs.org gallery)

| # | Format | Looks like | Best for |
|---|---|---|---|
| 8 | **3D product hero film** | One object, studio light, macro details, slow orbit, feature callouts | Launching a product or app feature |
| 9 | **Tiny world diorama** | A miniature low-poly town on a floating base, toy colours, camera dives in | Before/after, "a street where every shop..." |
| 10 | **3D kinetic typography** | Giant words as 3D slabs flying, stacking and turning (Arabic via stacked canvas planes) | Hooks, slogans, launches |
| 11 | **Particle and data globe** | Thousands of glowing points forming a map, globe or logo; arcs between cities; counters | Growth numbers, coverage, "X shops joined" |
| 12 | **Satisfying physics loop** | Jelly, marbles, stamps dropping and settling, seamless loop | Loop posts, stamp cards filling up |
| 13 | **Toon vehicle / chase cam** | Car or scooter on a road, chase camera, city sliding by, timer HUD | Delivery, "POV: your route", races |
| 14 | **Glass, liquid and macro** | Drinks, bottles, snow globes, refraction | Food and drink, perfume |
| 15 | **Cozy room / retro desk story** | One warm room, objects tell the story, dust in the light | Day-in-the-life of an owner, brand origin |

Details, gallery links, example ideas and three.js recipes (deterministic physics, particles, glass, Arabic 3D
type) are in `references/threejs-formats.md`.

### Styles (the look), built in Blender or three.js

A format is the structure; a style is the look. Combine them: "format × style".

| # | Style | Looks like | Engine |
|---|---|---|---|
| S1 | **Gulf heritage** | Sadu weave, geometric patterns, gold on indigo, lantern light | Blender |
| S2 | **Claymation stop-motion** | Plasticine, fingerprints, 12 fps stepped motion | Blender |
| S3 | **Papercraft** | Layered paper cut-outs with real soft shadows | Blender |
| S4 | **Neon Gulf night** | Neon signs, wet reflective streets, haze | Blender |
| S5 | **Apple-keynote product** | White/graphite studio, glossy hero object | three.js / Blender |
| S6 | **Clay miniature diorama** | Toy town, tilt-shift, soft dusk | Blender |
| S7 | **Toon cel + ink outlines** | Game-engine cartoon, black outlines | Blender / three.js |
| S8 | **Flat vector 3D** | Flat-shaded, orthographic, one hot colour | three.js |
| S9 | **Isometric pastel** | Floating isometric rooms, pastel gradients | three.js |
| S10 | **Pixel art retro** | Low-res render scaled up sharp | three.js |
| S11 | **Hand-drawn sketch** | Ink lines drawing themselves (Grease Pencil) | Blender |
| S12 | **Risograph print** | Two-ink grain, halftone, misregistration | three.js / Blender |
| S13 | **Vinyl toy cinematic** | Toy figures, film light, shallow DOF | Blender |
| S14 | **Kinetic 3D typography** | Giant 3D words, hard cuts | three.js |

Palettes, materials, light, camera, motion, type and the Blender/three.js recipe for each are in `references/styles.md`.

## Arabic voice (ElevenLabs)

- Use `eleven_v4`, `language_code: "ar"`, `apply_text_normalization: "on"`, narration settings stability 0.7 /
  similarity 0.5, and `previous_text`/`next_text` stitching. v4 ignores `speed`: pace with punctuation (every «…»
  adds a pause), and fit lines with ffmpeg `atempo` (max about 1.15).
- Write numbers as words, add tashkeel only on words the model may misread, put a comma after short words that
  blend into the next («بَسّ،»), and avoid one-word lines («ليش؟» → «ليش يعني؟»).
- Always verify: transcribe each line back with Whisper (faster-whisper large-v3-turbo, local) and diff against the
  script with diacritics stripped. Do not give Whisper a text hint on very short clips (it echoes the hint).
- Record the voice FIRST, then cut the picture to the real line timings.

## Before building

- Ask (or infer) only: format, language (Arabic needs browser-shaped text, right-to-left), length (15 to 60 s), voice or no voice, CTA.
- Write the script as a table: time, what we see, on-screen text / speaker. Mark HOOK and REHOOK. Get a yes.
- Use REAL assets of the product (screens, logo, mascot) whenever a phone or sign appears.
- Never use AI video models (Kling, Seedance, Wan, Higgsfield video, etc.) unless the user asks for them. Everything here is built and rendered locally.

## Toolkit

Needs Node 22+, Python 3, ffmpeg; Blender 4.2+ with a GPU for the Blender styles.

- **HyperFrames** (HTML + GSAP to MP4): `npx --yes hyperframes@0.8.181 render <dir> -o out.mp4 -q draft|high`,
  `... snapshot <dir> --at 0,3,6 --no-end -o stills`. One root `#root[data-composition-id=main][data-duration][data-width=1080][data-height=1920]`,
  one paused timeline. Use `scripts/studio.js` (`STUDIO.play(t => render(t))`): same time in, same picture out
  (no Math.random, Date.now, timers). Video clips: `<video class="clip" src=... data-start data-duration muted playsinline>`.
- **three.js** in HyperFrames: `https://cdn.jsdelivr.net/npm/three@0.149.0/build/three.min.js` (classic script).
  Upload every image texture through a 2D canvas first (direct `<img>` textures render blank).
  `preserveDrawingBuffer: true`. Drive AnimationMixer from the clock, never from real time.
- **Blender** (GPU, EEVEE), run headless: `blender -b -P script.py` (on Windows the exe is under
  `C:\Program Files\Blender Foundation\Blender <version>\`).
  Toon: Shader to RGB + constant ColorRamp; outlines: Line Art or inverted hull. Blender text cannot shape Arabic:
  render Arabic words to PNG in a browser and use them as textures; put subtitles on afterwards in HyperFrames.
- **Free 3D kits (CC0, Kenney)**: download from OpenGameArt (`opengameart.org/content/<kit>`; kenney.nl blocks scripts).
  `mini-characters` GLBs are rigged with animations (idle, walk, sprint, emote-yes/no, interact, holding, sit...),
  `city-kit-commercial / roads / suburban` for streets and shops. Keep one shared copy in an `assets3d/` folder
  next to your video projects.
- **Arabic type**: Google Fonts `Lalezar` (posters), `Tajawal` 500/800 (UI, subtitles); canvas `ctx.direction='rtl'`.
- **Voice**: ElevenLabs (`eleven_v4`), key only in a `.env` (`ELEVENLABS_API_KEY=`), never in chat.
  `scripts/tts_elevenlabs.py` (copy it into the project's `audio/` folder next to a `vo.json`): `voices`, `lines`, `mix`.
- **Checks**: `python -I scripts/pacing_check.py out.mp4 --end-hold 1.5` (no dead gap over 1 s, nothing under 0.3 s),
  `scripts/loop_check.py` for loops. Always look at stills at every beat before the full render.
- Windows: install ffmpeg with `winget install Gyan.FFmpeg`; in an already-open PowerShell refresh PATH first:
  `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`.
- Reference reels: `python -m yt_dlp -o ref.mp4 <instagram url>` (public reels), then
  `ffmpeg -i ref.mp4 -vf "fps=1/3,scale=150:-2,tile=12x3" -frames:v 1 sheet.jpg` and read the sheet.

`scripts/pacing_check.py`, `_media.py`, `loop_check.py`, `studio.js` come from the MIT-licensed claude-video-2 skill
(`scripts/LICENSE-claude-video-2.txt`).
