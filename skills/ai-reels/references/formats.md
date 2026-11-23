# The 7 formats in detail

Each section: the reels it comes from, what is on screen, the beat structure, the text system, overlays, the end,
how to build it here, and the traps. Timings are from the real reels.

---

## 1. Toon POV story

**From**: instagram.com/reel/Df-CuHrsdqM (survival road trip, 141 s), instagram.com/reel/DfrqJyNosyX (classroom hiding,
Part 2, 68 s), instagram.com/reel/DgEK-NCNMwj (POV date at a restaurant, blocky variant, 95 s).

**Picture**
- Game-engine 3D, cel-shaded: 2 to 3 flat tones per material, black ink outlines on everything.
- Low-poly world: roads with lane lines, sidewalks, simple houses/shops, blob trees, power lines; muted warm sky
  (khaki/ochre), or deep blue for night/interiors.
- FIRST PERSON: your sleeves and hands at the bottom of the frame, holding a phone, a gun, a card. Wide lens
  (16 to 20 mm), edges bend a little. Handheld sway, walking bob, quick head turns.
- Characters walk up, stop, face camera, talk. Eyes big and white so they read small.
- Floating paper bits / ash / dust in the air.

**Beats**: chapter card "DAY 1 / Somewhere in New Jersey" (big bold white + small line, left side; for Arabic put
it on the right) every 20 to 40 s; dialogue lines 1.5 to 3 s each; a phone chat appears full-height in your hand
for texts (rounded app UI, bubbles, red "DON'T OPEN" style warnings).

**Text**: small bold subtitles centred at about 60% height, one line, colour per speaker (white = you, yellow =
friend, pink/cyan = others), thin dark outline. The blocky variant also flashes ONE big caps word in yellow
(HE'S / HOW / STARING) for the narrator, with italic small subtitles for dialogue.

**End**: "WHAT WOULD YOU DO?" with two buttons (green RUN / red STAY), "Comment for Part 3". Next part opens with
"PART 2 / You chose: KEEP IT LOCKED".

**Build**: Blender (EEVEE + Shader to RGB toon + Line Art) or three.js (MeshToonMaterial + inverted-hull outline);
Kenney mini-characters (animated) + city kits; POV arms from capsules parented to the camera; subtitles and cards
on an HTML canvas overlay.

**Traps**: outlines too thin at 1080 px (use 2.5 to 4 px); characters floating (ground them); subtitles over a face.

---

## 2. "What if" life sim

**From**: instagram.com/reel/DfDOGC3BP0k ("What if you could stop time?", 119 s).

**Picture**: semi-realistic game characters (Unity/Unreal look), real-world sets (street, hotel, classroom, Paris,
pyramids, wedding, kitchen), slightly flat lighting, frequent cuts (2 to 4 s).

**Beats**: title in pixel/mono caps over the first shot ("WHAT IF YOU COULD STOP TIME?"), then a life told in
2nd person ("You pull her back to the curb, and press play."). The HUD counts up through the video
(AGE 24 / LIVED 24 YEARS, DAY 1 → DAY 90, PAUSE ▌▌ / PLAY ▶) and the gap between two counters IS the story.
Twist at about 70% ("One day, you can't remember her voice.").

**Text**: monospace/pixel typewriter subtitles, 2 lines, white with shadow, at about 70% height.
HUD top centre in pixel font.

**End**: the question again ("Would you press PAUSE?") + YES / NO in the caption for comments.

**Build**: three.js or Blender scenes with Kenney characters (less real, which is fine), HUD + typewriter in HTML.

**Traps**: keep the counter logic consistent; one idea only.

---

## 3. Illustrated "You decide" thriller

**From**: instagram.com/reel/Df-JfjhNdm4 ("Your bank sent you $750 million by mistake", 75 s).

**Picture**: painted digital illustrations (thick lines, moody teal/amber light) of a simple cartoon character
(white round head, beanie), each still pushed in slowly or panned; inserts of realistic phone UI (bank app balance,
"URGENT: Funds deposited in error" email, Google search results, news), a mugshot board.

**Beats**: new picture every 1.5 to 2.5 s. "REAL STORY" date tags in red pills ("AUG 2020 – REAL STORY") to bring
in true cases as proof, then back to you. Rising pressure: countdown in the HUD.

**Text**: bold caps captions, 2 to 4 words, centred low, key word coloured (yellow = money/number, red = danger).
HUD bar at the top: BALANCE $750,000,011 | TIME LEFT 23:48:14 | SUSPICION 0% → 100%.

**End**: dark card "WHAT DO YOU DO?", option A and B as image buttons, "COMMENT A OR B / The majority writes Part 2",
countdown digits 4…1, "FOLLOW FOR PART 2" red pill.

**Build**: illustrations must be real art (the user's, or drawn in SVG); phone UIs as HTML; HyperFrames for push-ins,
HUD counters and captions. For a product, the phone UI is the real app screen.

**Traps**: keep claims true; "REAL STORY" only for real, checkable events.

---

## 4. Flat vector motion comic

**From**: instagram.com/reel/Df5NY-WpLPr (trucker, "The 1% load – Part 1", 53 s), instagram.com/reel/De2tNL0vSUj
(nuclear alert in a supermarket, 100 s).

**Picture**: flat vector art, no outlines or thin ones, limited palette (navy night + one orange/yellow, or warm
greys + red). Big faces, simple shapes, rain lines, bokeh lights. Phone text threads drawn huge in a hand.
Diagrams: cutaway of a basement ("THICK CONCRETE WALLS"), supplies counted on screen.

**Beats**: a cut or a move every 1.5 to 2 s; clock stamp top-left ticks (3:00 AM → 3:08 AM); series tag top-right
("THE 1% LOAD · PART 1"). Survival version: stats HUD (HOUR 00/72 · WATER 12 L · FOOD 18 CANS · OUTSIDE FALLOUT) and
a big countdown "71:39:14 HOURS TO SURVIVE THE FALLOUT".

**Text**: bold caps captions low-centre, 2 to 3 words, one key word in orange or red.

**End**: "WHAT DO YOU DO?" A / B outlined buttons, "COMMENT A OR B", "FOLLOW FOR PART 2", brand mark. Door
version: two doors labelled OPEN / SHUT with the characters behind them.

**Build**: fully in code: SVG characters and sets in HyperFrames, GSAP moves, HUD in HTML. Cheapest format to make.

**Traps**: keep characters on-model (reuse the same SVG parts); do not overcrowd the HUD.

---

## 5. Cinematic toy-figure 3D

**From**: instagram.com/reel/Dfu_iARqY25 ("RUNWAY – Part 4", Play WW3, 102 s).

**Picture**: rendered 3D with vinyl/clay toy people (round white heads, big black eyes, helmets), cinematic lighting
(red alarm light, green map glow), shallow depth of field, then a bright jungle runway; props: steel bunker door,
map screens, small plane, cockpit switches, drone thermal view ("HUMAN DETECTED").

**Beats**: opens on last part's vote: real comments pop up over the scene ("KEEP IT SHUT" with likes). Dialogue in
quotes and narration ("You run to the plane..."). Choice buttons placed IN the scene near the thing they mean
("HELP HIM" over the person, "LEAVE" over the plane).

**Text**: small white subtitles low-centre, quotes for speech, plain for narration.

**Build**: Blender EEVEE with DOF, simple rigged figures (capsule bodies, sphere heads), emissive lights;
overlays in HyperFrames.

**Traps**: render time; keep shots short and few; reuse sets.

---

## 6. Roblox-style narrated story

**From**: instagram.com/reel/DflKPTcKK1M ("The Ice Cream Truck Only Comes at Midnight", 148 s),
instagram.com/reel/DfN6kYPqjUG ("The Rich Live Above the Clouds – Part 1", 120 s).

**Picture**: blocky avatars (Roblox-like proportions), bright saturated toy worlds (neon-pink truck interior, sky
city of glass towers vs a poor dirt ground), dramatic angles (low angle up skyscrapers, top-down neighbourhood),
fast cuts every 1 to 2 s, an occasional giant face close-up for emotion.

**Beats**: narrator tells it in past tense ("Mason grabbed...", "nobody..."). Rules shown as a list on screen early
("RULES 1. ... 2. ..."). A mystery, then a reveal, then a cliffhanger note ("BUT WHO'S GOING TO FREE ME?").

**Text**: ONE word at a time, big, centred, yellow-green fill with black stroke (key words) or white, exactly synced
to the voice (use the TTS word timings).

**Build**: three.js or Blender with blocky characters (Kenney mini-characters / blocky-characters, or boxes),
simple bright sets; word timing from ElevenLabs alignment output.

**Traps**: do not copy Roblox branding or real Roblox characters; keep the blocky look generic.

---

## 7. Cartoon dialogue explainer

**From**: instagram.com/reel/Df90iTCD9du (CharmXP, "What to do when she mentions her ex", 57 s).

**Picture**: flat 2D cartoon pair (orange hoodie / purple jacket) on a night street with warm shop windows; the same
set all video; poses change on every line; occasional over-the-shoulder close-up.

**Beats**: LEVEL 1 → 5. Each level replays the same moment with one more rule; the HUD shows the rules learned
(✗ dig for details, ✓ don't dig, ✓ keep it light, ✓ bring it back to now) and a progress meter. Wrong moves get a
red/orange stamp ("INTERROGATION 💀", "WENT COLD", "BROUGHT HIM BACK"), plus "AWKWARD SILENCE 0:03".

**Text**: fixed title header two lines ("What to do when / she **mentions her ex**", key words orange); speech
bubbles in caps above the speaker.

**End**: the right version plays out, then the brand line ("PRACTISED ON CHARMXP").

**Build**: SVG characters with swappable arm/face poses in HyperFrames; bubbles and HUD in HTML. Great for product
how-tos (wrong way vs right way, then "with <product>").

**Traps**: keep the rule list short (max 4); the last level must feel like a win.

---

## Shared engagement devices (use 1 or 2, not all)
- Part numbering and "You chose: X" openers; "the majority writes Part 2".
- Live counters in a HUD (money, time left, hours, age, suspicion %).
- Phone inserts (texts, bank app, notification) as the plot turn.
- Coloured key words in captions (yellow = value, red = danger, orange = brand).
- Comments from the previous part shown on screen.
