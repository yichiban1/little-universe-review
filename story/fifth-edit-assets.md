# Fifth edit material and typography

All retained screenshots, photographs, official promotional material and sound sources retain the provenance documented in `fourth-edit-assets.md` and `sources.md`. No generated or stock image was added. The fifth pass reduces the used original-image count rather than pursuing more files.

## One additional web state

Source: [the actual reviewed X Doctor 2008 episode](https://www.xiaoyuzhoufm.com/episode/666fd8d7c26e396a3656f1e0), inspected 26 September 2026.

- `analysis/fifth-research/web-xdoctor-playing-raw.png`: actual browser capture after starting the episode. DOM inspection showed an audio duration of 11277.456 seconds, current time advancing past 25.526 seconds, `paused: false`, `readyState: 4`. The visible saved transport reads 00:41 and shows its pause button. This is current web playback evidence; no episode audio was copied into the film.
- `public/assets/web-xdoctor-playing-page-fifth.png`: original capture rectangle `(202,46)–(774,608)`. Browser chrome, comment identifiers and QR sidebar are excluded.
- `public/assets/web-xdoctor-playing-controls-fifth.png`: original capture rectangle `(0,847)–(974,916)`.
- The film places page and transport fragments separately as editorial details. Their separation is intentional; they are not presented as an unedited full-screen capture. Both fragments count as one original source and one X Doctor episode family.
- Personal narration about English listening elsewhere and preferring the phone is user-supplied usage judgement. It does not establish a lack of English shows or a missing web player. No competitor mark is used.

The published episode page was rechecked: 03:45 is a real outline time; the Olympic-era photograph, DVD-shop photograph and the two quoted listener memories are in that episode. The mobile notes screenshot stops at the timeline heading, so the enlarged 03:45 remains an editorial annotation from the published notes, not a captured mobile button. 02:33 is separately the user's captured playback/input state.

## Local fonts

Installed packages, locked in package-lock.json:

- `@fontsource-variable/inter` 5.3.0: Inter Project Authors, SIL Open Font License 1.1.
- `@fontsource-variable/inter-tight` 5.3.0: Inter Project Authors, SIL Open Font License 1.1.
- Bundled Latin variable WOFF2 files and their original license texts are in `public/fonts/`.
- `src/fifth-fonts.ts` uses Remotion's render-blocking `loadFont()`; no network font request is needed during rendering. Inter Tight supplies editorial display text; Inter supplies labels and captions. Screenshot typography remains pixels from the source.

## Preserved originals

`analysis/fifth-research/fourth-preservation.json` records SHA-256 hashes of 142 fourth-related source, script, story, audio, analysis and output files, plus the shared public assets. Verification is part of fifth QA. CODEX_HANDOFF and the composition registry are intentionally updated for the new version.
