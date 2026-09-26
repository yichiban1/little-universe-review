# Third edit: directed shot plan

## Diagnosis

The second edit divides nearly every beat into five equal shots, resets the whole canvas at each boundary, and animates a sine-wave waveform. This makes timing, motion, and sound feel generated. The train stock photo is disproportionate to the app review. Podcast covers often leave their feed context. X Doctor green overwhelms Little Universe's cyan, black, and white identity. These are edit decisions, not missing effects.

## Editorial rules

- Source of truth: the six supplied current app screens. Public App Store promotional screens are examples of platform presentation; they are not presented as the user's exact current screen.
- Timing: word-aligned voice boundaries, with individually chosen shot starts and ends. No equal division by beat. Brief cutaways vary with 3–5 second holds.
- Visual motion: screen navigation and image enlargement have a cause; a held photograph stays still. Fast interface movement has a short settle; large photographs never bounce. No endless opacity, rotation, or waveform loops.
- Identity: use Little Universe's cyan for emphasis and UI context; X Doctor green belongs only to X Doctor material and actual player screenshots.
- Evidence stays attached to its source: episode covers only in discovery/search UI; photographs grow out of the Show Notes screen; comment details remain in the comments screen. Source and license caveats belong in `sources.md`.
- Sound: one continuous voice; quiet music with section-level dynamics; recorded and licensed tactile SFX only at actual taps, search, and photo movements. Some transitions remain silent.

## Intended visual arc

1. **Opening, 0–19.22 s:** X Doctor artwork and video thumbnail; a search field pulls the story into the user's real Little Universe player. Fast peeks at notes and comments; app title lands at 18.04 s. The old App Store search example is not shown as if it were the user's X Doctor search.
2. **Player, 19.22–40.72 s:** real player, from full screen to tight artwork, episode title, timeline, and rewind. The rewind tap is one event at 35.09 s. The waveform comes from narration samples.
3. **Discovery, 40.72–61.25 s:** official App Store feed and search examples, with covers inside recognisable feed/search context. Daqing is a personal spoken observation, never claimed as a screenshot we have.
4. **Listening, 61.25–72.69 s:** real player and recorded voice waveform; no commuter stock montage.
5. **Show Notes, 72.69–107.07 s:** player → episode information → scroll through outline → two additional photographs from the official published notes → Olympic image expands at 86.44 s → contracts to notes as DVD-shop photo expands at 88.62 s → episode page. This is the longest sequence.
6. **Comments, 107.07–136.42 s:** 02:33 player → comment box with the same playback time → two real listener comment crops → back to 02:33. The comments themselves are not falsely represented as posted at 02:33.
7. **History, 136.42–155.97 s:** profile listening total, then sticker shelf. Keep total time distinct from the one-creator 100-hour sticker.
8. **Ending, 155.97–178.95 s:** feed → notes → X Doctor/player → saved notes and comments → listening record → actual app icon. No repeated slogan.

All 58 individual shot anchors, starts, ends, and word indexes are in `src/shots-third.json`; change a spoken phrase in `scripts/build_third_shots.py` to regenerate the timeline after a voice edit. The six motion-review clips in `analysis/third-motion-*.mp4` cover opening, player, discovery, Show Notes, comments, and ending.

## Voice and sound

Two sample reads of the opening were rendered: `voice-sample-third-jenny.mp3` (8.69 s) and `voice-sample-third-andrew.mp3` (7.13 s). The third edit uses a single Andrew master at -10% rate for a measured 178.95 s film. The voice has word boundary data in `src/words-third.json` and an RMS envelope in `src/voice-envelope-third.json`. The samples are preserved for a human listening comparison. External music and recorded sounds, with their individual licenses and trim decisions, are documented in `sources.md`.
