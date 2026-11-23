# AI Reels

**A Claude Code skill for making scroll-stopping vertical videos (Reels, TikTok, Shorts) entirely in code.**
No AI video models: every frame is built and rendered locally with HyperFrames (HTML + GSAP), three.js and Blender,
using free CC0 3D assets and your real product screens.

The skill is a catalogue of **15 video formats**, each with what it looks like, the beat structure (hook in 1.5 s,
rehook at about 40%, payoff, end card), the caption system, overlays, and a build recipe.

### Story formats (studied from real viral reels)
1. **Toon POV story**: cel-shaded 3D, black outlines, first person with your hands in frame, "DAY 1" chapter cards
2. **"What if" life sim**: 2nd-person narration, HUD counters (AGE 24 / LIVED 30 YEARS / PAUSE)
3. **Illustrated "You decide" thriller**: painted stills, phone UI inserts, money/time HUD, A or B ending
4. **Flat vector motion comic**: clock stamps, big text-message screens, survival stats, countdowns
5. **Cinematic toy-figure 3D**: vinyl figures, moody light, vote comments and choice buttons in the scene
6. **Roblox-style narrated story**: blocky avatars, bright worlds, one big word at a time synced to the voice
7. **Cartoon dialogue explainer**: speech bubbles, LEVEL meter with wrong/right rules, stamp labels

### 3D showcase formats (inspired by the threejs.org gallery)
8. 3D product hero film · 9. Tiny world diorama · 10. 3D kinetic typography · 11. Particle and data globe ·
12. Satisfying physics loop · 13. Toon vehicle / chase cam · 14. Glass, liquid and macro · 15. Cozy room / retro desk story

## Install

```bash
npx skills add krispx2811/ai-reels
```

or copy `skills/ai-reels/` into `~/.claude/skills/ai-reels/`.

Then in Claude Code: "make me a reel about ...", "what kinds of videos can you make?", or `/ai-reels`.

## What you need
- Node 22+, Python 3, ffmpeg
- Optional: Blender 4.2+ with a GPU (for the Blender-rendered 3D formats)
- Optional: an ElevenLabs API key for voiceover (kept in a `.env`, never in chat)

## What's inside
```
skills/ai-reels/
  SKILL.md                      format picker + toolkit
  references/formats.md         the 7 story formats in detail
  references/threejs-formats.md the 8 3D showcase formats in detail
  scripts/studio.js             one-clock helper for deterministic HyperFrames renders
  scripts/pacing_check.py       measures dead gaps and flashes from the rendered pixels
  scripts/loop_check.py         proves a loop is seamless
  scripts/tts_elevenlabs.py     ElevenLabs voice lines, timed and mixed onto the video
```

## Credits
- `studio.js`, `pacing_check.py`, `_media.py`, `loop_check.py` come from the MIT-licensed claude-video-2 skill
  (see `scripts/LICENSE-claude-video-2.txt`).
- Reference reels and three.js gallery projects are linked, not copied; all rights stay with their creators.
- Recommended free 3D assets: [Kenney](https://kenney.nl) (CC0).

## License
MIT
