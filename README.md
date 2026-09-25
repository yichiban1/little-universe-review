# Little Universe — personal app review

An editable 1920×1080, 30 fps Remotion first cut, approximately 3:03. The spoken narration is in English and calls the app “Little Universe.”

## Outputs

- `out/little-universe-review-final.mp4`: final submission MP4
- `out/narration.mp3` and `out/narration.md`: isolated voice and final script
- `out/captions.srt`: timed English captions
- `out/little-universe-review-project.zip`: source, assets and final deliverables without `node_modules`
- `src/captions.json`: caption source data
- `story/reference-analysis.md`: reference method analysis
- `story/sources.md`: citations and asset provenance

## Edit and render

Requires Node.js and npm.

```powershell
npm install
npm run dev
npx remotion render src/index.ts LittleUniverseReview out/little-universe-review-final.mp4 --codec h264 --crf 22 --pixel-format yuv420p --audio-codec aac --audio-bitrate 192K
```

The editable scene components live in `src/Scenes.tsx`; shared visual rules are in `src/Design.tsx`. The narration and beat timing are in `story/beats.json` and `src/timing.json`. The audio and selected screenshot derivatives are already bundled in `public/`, so generation scripts are optional. The music source is `scripts/make_music.py`. The captions and isolated narration may be re-exported using `python scripts/export_deliverables.py`.

The film's factual distinction: 128 h 27 m is the supplied profile's overall listening time. The 100-hour sticker is described as a reward for time with one creator. No claim connects those two counts.

The film also uses official App Store promotional screens and two AI-generated editorial illustrations. Both illustrations are conceptual; `story/sources.md` records their provenance and the real product sources.
