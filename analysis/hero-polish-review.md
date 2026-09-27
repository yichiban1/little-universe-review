# Final Hero Polish selection

Base: accepted `hero-pass` at `cce5f49`. Isolated local branch: `hero-polish`.
Final composition: `LittleUniverseReviewHeroPolish`. Original Hero and Sixth
remain available unchanged. The rejected Critical experiment is not included.

| Sequence | Decision | Editorial judgement from A/B and native transition review |
|---|---|---|
| Player | Keep polish | The fixed artwork anchors the observation, which yields its column before disappearing. “2008” enters during that handoff, aligns with the artwork top, and the real metadata excerpt grows beneath the same alignment. There is no empty intermediate state. Context clears earlier on return, so the phone takes visual ownership while the same artwork follows its accepted path and lands at the original bounds. |
| Discovery | Keep polish | The detached row retires during catalogue entry; the Ritan page leaves by 52.750s, rather than remaining behind Sound. Ritan becomes a small, subdued earlier-stop marker before the blue identity appears. The blue cover establishes attention before its catalogue grows in; Sound retires by 56.100s. Episode context replaces programme context, rather than retaining both pages. The earlier-stop marker clears before the unchanged Daqing shot. |

The improvement is continuity and attention hierarchy, not additional animation.
No text, imagery, sound, font or colour system was added. Existing meaningful
holds and the main artwork trajectory remain. Outside Player frames 658–1016
and Discovery frames 1391–1777, the shot implementation directly calls `HeroShot`.

## Review evidence

- `hero-polish-player-comparison.mp4` and `hero-polish-discovery-comparison.mp4`: **current Hero left / final Polish right**, with matched frame intervals.
- `hero-polish-player-strip.jpg`, `hero-polish-discovery-strip.jpg`: final-encode overview, labelled with absolute film times.
- Six `hero-polish-framebyframe-*.jpg` sheets: every 30fps frame around text yield, phone return, browse, branch, episode replacement and route resolution.
- `hero-polish-native/`: 26 encoded 1920×1080 frames, including overlapping text and return/branch geometry.
- `hero-polish-full-strip.jpg`: whole-film context, including preserved later chapters and ending.
- The full final MP4 played from 0 to 184.042667s at 1x and reached `ended:true`, with no media error. Visual samples were checked during playback; motion decisions also use the actual short encodes and frame-by-frame sheets. See `hero-polish-playback.json`.

This was a visual review plus technical audio preservation check. Playback was
muted; there is no new claim about Andrew voice naturalness or auditory quality.
The accepted audio was preserved exactly.

## Preservation and technical QA

- `npm run lint` and `git diff --check` pass.
- 929 original tracked/output files pass exact SHA-256 preservation, including original Hero/Sixth renders and original QA. The original checkout's user `.gitignore` edit remains intact.
- 20 protected native source frames, including entry/exit boundaries and later chapters, are PNG-byte-identical to Hero. All other shots still delegate to Hero. This does not assert identical compressed packets in the new H.264 encode.
- Film wrapper, audio, caption and timeline code match Hero after normalizing component/import names and trailing blank lines.
- 13 raster source dimensions verified. Original crop, resolution and phone-geometry helpers are preserved. Maximum new UI scale is 650/600 = 1.0833x; artwork maximum is 810/1440 = 0.5625x. Existing inherited limits remain active.
- Full video/audio decode passes. 1920×1080, 30fps, 5520 video frames, 184.042667s, 29,398,804 bytes.
- AAC payload matches Hero exactly: `61a3997ba976d6b4e6f483cd1539764b`.
- `captions-hero-polish.srt` is a byte-identical copy of the accepted Hero captions.
- Master SHA-256: `bb3a5fa55f3733211cd3b2b0e556b7ef41f749c29b464b92947416e773bf46a0`.

Final master: `out/little-universe-review-hero-polish-edit.mp4`.
Convenient duplicate: `E:\App review\little-universe-review-hero-polish-edit.mp4`.
Both have the same SHA-256. The branch is local; no remote branch or PR was changed.

## Rebuild

Run from the isolated checkout:

```
npm run lint
npx remotion render LittleUniverseReviewHeroPolish out/little-universe-review-hero-polish-edit.mp4 --codec=h264 --crf=16 --image-format=png --concurrency=4 --log=error
python -X utf8 scripts/qa_hero_polish.py --master
python -X utf8 scripts/qa_hero_polish.py
node scripts/check_hero_polish_frames.cjs
```

Only the new polish builders should run. Existing Sixth/Hero builders can rewrite
frozen QA/output files and were not used for this pass.
