# Little Universe — personal app review

An editable 1920×1080, 30 fps Remotion second edit, approximately 2:47. The continuous English narration calls the app “Little Universe.” The former first cut remains in `out/` for comparison if present.

## Outputs

- `out/little-universe-review-second-edit.mp4`: revised review draft
- `out/narration.mp3` and `out/narration.md`: isolated voice and final script
- `out/captions.srt`: timed English captions
- `out/little-universe-review-project.zip`: source, assets and final deliverables without `node_modules`
- `src/captions.json`: caption source data
- `story/reference-analysis.md`: reference method analysis
- `story/revision-plan.md`: second-edit shot and sound plan
- `story/sources.md`: citations and asset provenance
- `analysis/second-edit-sheet-1.jpg` through `-4.jpg`: approximately 2-second QA contact sheets

## Edit and render

Requires Node.js and npm.

```powershell
npm install
npm run dev
npx remotion render src/index.ts LittleUniverseReview out/little-universe-review-second-edit.mp4 --codec h264 --crf 18 --pixel-format yuv420p --audio-codec aac --audio-bitrate 192K
```

The second edit lives in `src/SecondEdit.tsx` and `src/Film.tsx`. The former `src/Scenes.tsx` and `src/Design.tsx` are kept as first-cut history but are no longer mounted. The narration and beat timing are in `story/beats.json` and `src/timing.json`. The audio and selected screenshot derivatives are bundled in `public/`. `scripts/generate_voice.py` produces one continuous voice master and word timing; `scripts/make_music.py` creates the evolving score and original cues. Re-export captions and narration using `python scripts/export_deliverables.py`.

The film's factual distinction: 128 h 27 m is the supplied profile's overall listening time. The 100-hour sticker is described as a reward for time with one creator. No claim connects those two counts.

The second edit uses actual user screenshots, official product and podcast imagery, and one licensed documentary commute photograph. The two AI-generated first-cut illustrations are no longer used. `story/sources.md` records provenance and reuse context.
