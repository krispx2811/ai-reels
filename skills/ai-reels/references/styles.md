# Styles (the look), built in Blender or three.js only

A **format** (SKILL.md) is the story structure; a **style** is the look. Any format can be rendered in any style,
for example "1. Toon POV story × Neon Gulf night". Every style here is built with **Blender** (EEVEE, GPU) or
**three.js** (inside HyperFrames). Arabic text is never typeset inside Blender: shape it in a browser, use it as an
image texture or composite it afterwards.

Each style lists: palette, materials, light, camera, motion, type, how to build it in Blender and in three.js,
best formats, and traps.

| # | Style | One line | Best engine |
|---|---|---|---|
| S1 | Gulf heritage | Sadu weave, geometric patterns, gold on indigo, lantern light | Blender |
| S2 | Claymation stop-motion | Plasticine, fingerprints, 12 fps stepped motion | Blender |
| S3 | Papercraft | Layered paper cut-outs with real soft shadows | Blender |
| S4 | Neon Gulf night | Neon signs, wet reflective streets, haze | Blender |
| S5 | Apple-keynote product | White/graphite studio, glossy hero object, perfect reflections | three.js or Blender |
| S6 | Clay miniature diorama | Toy town, tilt-shift, soft dusk | Blender |
| S7 | Toon cel + ink outlines | Game-engine cartoon, 2-3 tone bands, black outlines | Blender or three.js |
| S8 | Flat vector 3D | Flat-shaded shapes, orthographic camera, one hot colour | three.js |
| S9 | Isometric pastel | Floating isometric rooms, pastel gradients | three.js |
| S10 | Pixel art retro | Low-res render scaled up sharp, limited palette | three.js |
| S11 | Hand-drawn sketch | Ink lines drawing themselves, marker fills | Blender (Grease Pencil) |
| S12 | Risograph print | Two-ink grain, halftone, misregistration | three.js (post shader) or Blender compositor |
| S13 | Vinyl toy cinematic | Toy figures, film lighting, shallow depth of field | Blender |
| S14 | Kinetic 3D typography | Giant 3D words, hard cuts, flat colour | three.js |

---

## S1. Gulf heritage
- **Palette**: indigo `#1B1F4B`, deep red `#8E1B1B`, gold `#D4A84B`, sand `#E8D9B5`, off-white `#F7F1E3`.
- **Materials**: woven Sadu bands (red/black/white diamonds) as tiling textures on cushions, tents, borders;
  8-point star and girih patterns as emissive or embossed gold; brushed brass lanterns; plaster arches.
- **Light**: warm lantern pools (orange point lights, soft shadows) against a cool indigo night; dust in the beams.
- **Camera**: slow dolly through arches, symmetric framing, gentle parallax of pattern screens (mashrabiya).
- **Motion**: slow, ceremonial; patterns that draw themselves (shader reveal), lanterns swaying 2-3 degrees.
- **Type**: Arabic display: Reem Kufi / Amiri (calligraphic), Tajawal for captions; gold key words.
- **Blender**: pattern textures from SVG (draw in a browser, save PNG), Displacement for embossing, EEVEE soft
  shadows + volumetric fog for beams, mashrabiya = array of cut panels (Boolean or alpha texture).
- **three.js**: pattern as a ShaderMaterial (tiled 8-point star), lantern PointLights, fog, instanced arches.
- **Best for**: Ramadan, Eid, National Days, premium brand stories, end cards.
- **Traps**: avoid religious text as decoration; keep gold to accents, not everything.

## S2. Claymation stop-motion
- **Palette**: saturated but soft (tomato, butter yellow, teal, cream), no pure black or white.
- **Materials**: clay = Principled BSDF, roughness 0.55, subsurface 0.05, plus a fingerprint/thumb-smudge normal
  map and tiny surface lumps (noise displacement). Slight colour variation per object.
- **Light**: a key softbox + bounce, like a tabletop set; shallow depth of field (macro feel).
- **Camera**: locked-off or slow slider moves, like a real stop-motion rig.
- **Motion**: animate normally, then make it STEPPED: keyframe interpolation = Constant at 12 fps
  ("on twos" at 24) or Blender's *Stepped Interpolation* F-curve modifier. Add a 1-2% per-frame "boil"
  (random scale/rotation jitter, seeded) for the hand-made wobble.
- **Type**: rounded, chunky (Fredoka / Lalezar), cut-out paper labels.
- **Blender**: Kenney characters re-materialled as clay; geometry nodes for lumps; Stepped modifier on all actions.
- **three.js**: same materials (MeshPhysicalMaterial + normal map), sample the clock at floor(t*12)/12.
- **Best for**: friendly product stories, kids/teen, satisfying loops.
- **Traps**: boil must be seeded (deterministic); too much boil looks broken.

## S3. Papercraft
- **Palette**: paper tones (kraft `#C8A27A`, cream `#F3E9D6`, coral, teal), one accent.
- **Materials**: thin extruded shapes (2-4 mm) with a paper fibre texture and a slightly rough edge; slight curl.
- **Light**: one strong directional light at a low angle so every layer casts a soft shadow on the one behind.
- **Camera**: frontal, orthographic or long lens; parallax push-in through the layers.
- **Motion**: pieces fold, slide and pop up on hinges (rotation from an edge), like a pop-up book.
- **Type**: cut-paper letters (Arabic words drawn in a browser → used as alpha cut-outs).
- **Blender**: Solidify on planes, Displace for curl, EEVEE soft shadows with small light radius, AO on.
- **three.js**: stacked ExtrudeGeometry layers, DirectionalLight with PCFSoftShadowMap, paper texture.
- **Best for**: elegant brand stories, how-it-works, origin stories.
- **Traps**: too many layers make the shadows mushy; keep 4 to 7 depth planes.

## S4. Neon Gulf night
- **Palette**: night `#0B0A1A`, neon orange `#FF5A1F`, magenta `#FF2E88`, cyan `#2BD9FE`, warm sodium `#FFB347`.
- **Materials**: neon tubes = emission (strength 8-20) on thin curves; wet asphalt = low roughness (0.1-0.2) with
  puddle mask; glass shopfronts.
- **Light**: everything lit by the signs; light haze (volume scatter) so glows bloom; rain streaks.
- **Camera**: low angle along the wet street, slow tracking, reflections doing half the work.
- **Motion**: sign flicker on beats, rain, steam from a café, cars passing (headlight sweeps).
- **Type**: Arabic neon (Lalezar / Reem Kufi drawn as tube outlines), glow behind captions.
- **Blender**: EEVEE ray tracing ON (reflections), compositor Glare (Fog Glow), Volume Scatter 0.01-0.03.
- **three.js**: MeshStandardMaterial metal/rough for the street, UnrealBloomPass (examples), rain as instanced lines.
- **Best for**: hooks, cafés and night shops, "the one glowing shop", nightlife.
- **Traps**: bloom eating the text; keep captions outside glow areas or add a dark plate.

## S5. Apple-keynote product
- **Palette**: white `#F5F5F7` or graphite `#111214`, one accent; product colours only.
- **Materials**: glossy glass phone, aluminium edges (metalness 1, roughness 0.25), real screen textures.
- **Light**: big soft studio lights (area lights / RoomEnvironment), crisp rim light, contact shadow.
- **Camera**: slow orbits, macro passes along edges, then a clean frontal hero; very smooth easing (no bounce).
- **Motion**: one move per shot; UI on the screen animates; callout labels with thin leader lines.
- **Type**: SF-like sans (Inter) + Tajawal; small, precise, lots of space.
- **Blender**: Cycles or EEVEE with ray tracing, HDRI studio, depth of field on macro shots.
- **three.js**: MeshPhysicalMaterial (clearcoat, transmission for glass), PMREM RoomEnvironment.
- **Best for**: feature launches, app UI, "3. product hero film".
- **Traps**: fake UI ruins it: always real screens; avoid busy backgrounds.

## S6. Clay miniature diorama
- **Palette**: dusk sky gradient (peach `#F6B38E` → violet `#5B4B8A`), warm windows `#FFB15C`, clay pastels.
- **Materials**: soft clay (roughness 0.6), no outlines; ground on a floating rounded slab.
- **Light**: warm low sun + cool sky fill; emissive windows; streetlights.
- **Camera**: high aerial with tilt-shift (small focus band, f/1.2-2.8 on a long lens), glides and dives.
- **Motion**: little characters walking on paths, lights switching on in sequence, cards popping above shops.
- **Blender**: EEVEE ray tracing + AO, compositor Glare, DOF; Kenney city kits re-materialled.
- **three.js**: BokehPass for tilt-shift, InstancedMesh for crowds.
- **Best for**: "9. tiny world diorama", local business stories, before/after.
- **Traps**: flat navy sky looks cheap; use a gradient. Make the hero window clearly the brightest thing.

## S7. Toon cel + ink outlines
- **Palette**: muted warm world (khaki sky, grey asphalt), saturated characters.
- **Materials**: Diffuse → Shader to RGB → ColorRamp (Constant, 2-3 steps); three.js MeshToonMaterial + gradient map.
- **Outlines**: inverted hull (Solidify, flipped normals, black backface material) 2.5-4 px at 1080, or Line Art.
- **Camera**: first-person wide lens (16-18 mm) with hands in frame, handheld sway.
- **Best for**: "1. Toon POV story".
- **Traps**: chibi characters dominate close-ups; keep hands/phones in frame for product shots.

## S8. Flat vector 3D
- **Palette**: night navy `#0F1A2E`, ink, cream, ONE hot colour.
- **Materials**: MeshBasicMaterial (unlit) or flat-shaded toon with 1 band; no textures except real screens.
- **Camera**: OrthographicCamera, frontal, hard cuts and slow pans; 2D-looking but true 3D depth for parallax.
- **Motion**: snappy (power4.out), characters as layered planes (head, body, arms) with pivot rotations.
- **Build**: three.js only (orthographic scene, layered planes, shapes from THREE.Shape).
- **Best for**: "4. flat vector motion comic", fast production.
- **Traps**: keep characters on-model by reusing the same part meshes.

## S9. Isometric pastel
- **Palette**: pastel gradients (lilac `#C9B6FF`, mint `#B8F2E6`, peach `#FFD6BA`), white edges.
- **Materials**: matte, slightly glossy toy plastic; soft AO.
- **Camera**: OrthographicCamera at the isometric angle (rotate X 35.264°, Y 45°), fixed; the world moves instead.
- **Motion**: rooms assemble from tiles, objects drop in with a small overshoot, step-by-step reveals.
- **Build**: three.js (Ortho + SoftShadows + SSAO) or Blender (Ortho camera, EEVEE AO).
- **Best for**: explainers, "how it works in 3 steps", onboarding.
- **Traps**: isometric reads small on phones; one idea per room.

## S10. Pixel art retro
- **Palette**: 16-32 colour limited palette (e.g. PICO-8-like); hard edges.
- **Build**: three.js renders into a low-res WebGLRenderTarget (e.g. 180 × 320), NearestFilter, drawn to a full-screen
  quad at 1080 × 1920; optional palette-quantise fragment shader + 2-colour dither. Blender: render 180 × 320 then
  ffmpeg `scale=1080:1920:flags=neighbor`.
- **Motion**: snap to whole pixels, 12-15 fps feel, chiptune-style beats.
- **Type**: pixel fonts (Press Start 2P / for Arabic draw at low res and scale with nearest).
- **Best for**: Gen-Z hooks, playful promos, game-style "levels".
- **Traps**: Arabic at low res breaks: render captions at full res on top.

## S11. Hand-drawn sketch
- **Palette**: paper `#FBF8F1`, ink `#1F1D1A`, marker fills (one accent + one neutral).
- **Build**: Blender Grease Pencil (Line Art modifier to turn 3D into ink lines, Build modifier to draw them on over
  time, fills as GP fills), or three.js with EdgesGeometry lines + a dash-offset reveal and a paper texture plane.
- **Motion**: strokes draw on, then fills wipe in; slight line wobble (seeded).
- **Type**: handwritten Arabic (Aref Ruqaa / Reem Kufi Fun) for labels.
- **Best for**: explainers, "7. dialogue explainer", whiteboard-style how-tos.
- **Traps**: drawing everything at once is noise; reveal in reading order.

## S12. Risograph print
- **Palette**: two or three inks (fluorescent pink `#FF48B0`, blue `#0078BF`, yellow `#FFE800`) on paper.
- **Build**: render normally, then a post pass: split into ink layers, halftone dots, paper grain, 2-6 px
  misregistration offset per ink. three.js: ShaderPass after the render. Blender: compositor (Separate colour,
  Pixelate/halftone via texture, Translate per channel, Mix Multiply with paper scan).
- **Motion**: poster-like, hard cuts, ink layers sliding into register on beats.
- **Best for**: events, music, artsy brands, posters.
- **Traps**: misregistration on text hurts reading; keep captions clean on top.

## S13. Vinyl toy cinematic
- **Palette**: film tones (teal shadows, warm highlights), one coloured light per scene (red alarm, green screen).
- **Materials**: glossy vinyl (roughness 0.25, clearcoat), big round heads, simple helmets/props.
- **Light**: practical lights in frame, strong contrast, volumetric haze; shallow DOF.
- **Camera**: cinematic lenses (35-85 mm), slow push-ins, over-the-shoulder.
- **Build**: Blender EEVEE (ray tracing, volumetrics, DOF); three.js possible but Blender looks better.
- **Best for**: "5. toy-figure cinema", serialized drama with votes.
- **Traps**: render time; reuse one set per episode.

## S14. Kinetic 3D typography
- **Palette**: 2 colours + 1 accent (e.g. ink on brand orange), flat ground.
- **Build**: three.js: Latin with TextGeometry; ARABIC by drawing each word on a canvas (browser shaping) and stacking
  8-12 copies 3-5 mm apart (darker behind) for extrusion, or extruding SVG paths of browser-shaped text.
  Camera flies through words; hinge flips with springs.
- **Motion**: one word per beat, slams, crops off frame edges on purpose.
- **Best for**: hooks, slogans, offers, "10. 3D kinetic type".
- **Traps**: more than 3 words on screen at once.

---

## Picking a style fast
- Premium brand / product → S5 Apple-keynote, S3 Papercraft, S1 Gulf heritage.
- Story with characters → S7 Toon, S2 Claymation, S13 Vinyl toy.
- Night / cafés / hooks → S4 Neon Gulf night.
- Local businesses / streets → S6 Clay diorama, S9 Isometric.
- Explainers → S11 Sketch, S9 Isometric, S8 Flat vector.
- Youth / playful → S10 Pixel art, S2 Claymation, S12 Risograph.
- Text-led hooks and offers → S14 Kinetic type.
