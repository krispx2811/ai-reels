# 3D showcase formats (from the threejs.org gallery)

Eight more video types, taken from the project gallery on threejs.org (looked at 2026-11-23; numbers are the
thumbnail order on that page, links are the live projects). All of them are built as three.js scenes inside
HyperFrames and rendered to MP4, so they inherit the reel spine (hook, rehook, end card) from SKILL.md.

Rules that apply to all of them (otherwise frames flicker or differ between renders):
- One clock: every position, rotation, colour, shader `uTime`, and mixer time is computed from `t` only.
- Seeded randomness only (`STUDIO.rng(seed)`), created once, never inside the render loop.
- Physics: never step a live engine during capture (frames can be seeked out of order). Either use closed-form
  motion (ballistic arcs, springs: `x(t)=A·e^(−ζωt)·cos(ωt)`) or PRE-BAKE the whole simulation at load time into an
  array per frame and look it up by `Math.round(t*30)`.
- Images go through a 2D canvas before becoming textures. Real product screens go on planes/phone meshes.
- `renderer.outputEncoding = THREE.sRGBEncoding`, `preserveDrawingBuffer: true`, pixel ratio 1, 1080 x 1920.
- Environment light without files: `new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment())`
  (RoomEnvironment is in `examples/js/environments/RoomEnvironment.js` for r149).

---

## 8. 3D product hero film
**Looks like**: one object, studio light, slow orbit, perfect reflections, macro detail, very clean background.
**Gallery**: #109 Porsche studio (dyadstudios.com/renderapp/porsche), #124 camera (camera-webgi.vercel.app), #121
jewellery (webgi-jewelry.vercel.app), #012 raspberry macro (raspberry.luruke.com), #119 design the next iPhone
(neal.fun/design-the-next-iphone), #102 keyboard key.
**Reel structure**: hook = extreme macro of a detail, pull back to reveal the whole product; 3 to 5 "feature
callouts" each with a camera move to that part + a short label line; end = hero angle + logo.
**Build**: MeshPhysicalMaterial (clearcoat, roughness 0.2 to 0.4), RoomEnvironment PMREM, a soft contact shadow
(blurred plane texture), camera on a CatmullRomCurve3 path with eased progress, slight depth-of-field fake via a
blurred background plane.
**Example (a loyalty-card app)**: the phone with the real wallet card on screen; callouts: "stamps fill by themselves",
"reminder on the lock screen", "no app".

## 9. Tiny world diorama
**Looks like**: a miniature low-poly island / town / room on a floating base, tilt-shift feel, toy colours, the
camera glides around and dives in.
**Gallery**: #053 island (susurrus.vercel.app), #054 snowy village, #062 cozy house (worawork.vercel.app), #066
planet (messenger.abeto.co), #105 toy town (haru-ni.net), #120 Coastal World (coastalworld.merci-michel.com), #129
Choo Choo World (choochooworld.com), #044 Tiny Skies (tinyskies.vercel.app), #011 glass-case diorama, #133 Wayfinder.
**Reel structure**: hook = the whole world tiny in frame with a question; dive to one shop; something changes
(lights turn on, people walk in); pull back: the whole street now glows. Great for "before / after".
**Build**: Kenney city kits on a rounded base, warm hemisphere + key light, fog, orthographic or long-lens camera
(30 to 35 deg FOV) for the miniature look, animated Kenney characters walking on spline paths.
**Example (a loyalty-card app)**: a Gulf street of shops (barber, perfume, gym, pharmacy); each shop that joins lights up and a
little wallet card pops above it.

## 10. 3D kinetic typography
**Looks like**: giant words as 3D slabs or layered planes that fly, stack, fold and turn; strong colour blocks.
**Gallery**: #018 Plain Sight (motion-pieces.pages.dev/plain-sight), #042 Japanese vertical type
(batwa.fukudapero.com), #072 Symphony of Vines (symphonyofvines.com), #069 W×D, #056 STORY, #097 io puzzle.
**Reel structure**: one word per beat, the camera travels through the words; the last word becomes the logo.
**Build**: Latin: TextGeometry/extruded font. ARABIC: draw each word on a canvas (shaping + RTL) and stack 6 to 12
copies of that plane 4 mm apart (darker copies behind) to fake extrusion; or extrude SVG paths exported from a
browser-shaped text. Camera dolly on a path, words hinge with spring easing.

## 11. Particle and data globe
**Looks like**: thousands of glowing points forming a globe, a map, a logo or a creature; data arcs between cities;
counters ticking.
**Gallery**: #063 globe with live numbers, #089 BFCM "watch the world shop live" (bfcm.shopify.com), #059 particle
dolphin (cyber-ocean.vercel.app), #015 galaxy (sojourner.artificialisabel.com), #022 wireframe, #136 ribbons
(fungui.resn.co.nz), #079 sun.
**Reel structure**: hook = the count ("1,240 shops joined this month"), points burst into a map of the Gulf; arcs fly
between Muscat, Dubai, Doha, Riyadh; counters climb; the points regroup into the logo.
**Build**: THREE.Points with a custom ShaderMaterial (size attenuation, additive blending), target positions
per formation precomputed, morph by `mix(a, b, ease(t))` in the vertex shader with a `uT` uniform; arcs as
QuadraticBezierCurve3 tubes with a dash offset driven by t. Only use real numbers.

## 12. Satisfying physics loop
**Looks like**: soft jelly, marbles, balls, blocks falling and settling, squash and stretch, perfect loops.
**Gallery**: #031 Jelly Baby (jelly.scottsun.io), #067 balls, #007 Lost Marbles (meticulai.com/games/lost-marbles),
#041 blob (cgw334.mount.jp), #070 tetris stack.
**Reel structure**: 8 to 12 s loop; stamps (coins, cups, scissors icons) drop one by one into a card until it fills,
the reward pops, everything resets to the first frame (prove with loop_check.py).
**Build**: pre-baked or closed-form physics (see rules above); squash/stretch = scale.y by velocity; jelly = vertex
shader wobble driven by a damped spring of t.

## 13. Toon vehicle / chase camera
**Looks like**: a car, scooter or train on a road, chase camera behind, speed lines, a city sliding by.
**Gallery**: #000 New York taxi (mrdoob.github.io/slop-newyork), #080 Great Taxi Assignment
(great-taxi-assignment.netlify.app), #085 PolyTrack (kodub.com/apps/polytrack), #001 Road Thruster, #013 Vector,
#019 train, #099 scooter.
**Reel structure**: "POV: you're delivering..." / a race against a timer HUD; stops at shops; finish line = payoff.
**Build**: Kenney city-kit-roads tiles laid along a spline, vehicle follows the spline (position + tangent), camera
on a lagged spring behind it, wheel spin from distance travelled, simple speed-line planes near the lens.

## 14. Glass, liquid and macro materials
**Looks like**: drinks, aquariums, snow globes, glass cases; refraction, caustic-like light, droplets.
**Gallery**: #020 jelly painting drink (mesq.me/jelly-painting), #024 aquarium, #101 snow globe, #047 tools,
#012 raspberry.
**Reel structure**: slow macro hero shots, very short text; good for food and beverage shops (juice, karak,
perfume bottles).
**Build**: MeshPhysicalMaterial with `transmission: 1`, `thickness`, `ior 1.33 to 1.5`, RoomEnvironment; bubbles
as small instanced spheres rising on seeded paths; liquid surface as a displaced plane.

## 15. Cozy room / retro desk story
**Looks like**: one warm room (desk, CRT computer, bed, shop counter), lamps, dust in the light, the camera
drifts between objects that tell a story.
**Gallery**: #131 retro desk portfolio (henryheffernan.com), #123 BBC Micro (virtual.bbcmic.ro), #049 Creative
Development Studio (shader.se), #064 bedroom (lumen-decor-studio.vercel.app), #134 developer room, #074 laundromat,
#104 The Hidden Papers (one-year.cosmicshelter.com), #125 Museum of Annoying Experiences.
**Reel structure**: "This is where a shop owner starts the day..."; each object = one beat (paper stamp cards in a
drawer, a phone buzzing on the counter, the screen showing the Customers list).
**Build**: one interior set (boxes + Kenney props), baked-looking warm light (hemisphere + 1 spot + emissive lamps),
dust as seeded instanced quads, camera dolly between 4 to 6 marks; real screens as emissive textures.

---

### Picking between the two families
- Story with characters and choices → formats 1 to 7 (SKILL.md).
- Product, brand, data or "satisfying" visuals → formats 8 to 15.
- They mix well: a story reel (1) can cut to a product hero (8) for the payoff, or end on a particle logo (11).
