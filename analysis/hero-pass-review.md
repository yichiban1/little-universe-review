# Hero pass selection

Final composition: `LittleUniverseReviewHero`. Experimental branch: `hero-pass`. Safety version remains `LittleUniverseReviewSixth` with all Sixth sources, output, soundtrack, captions and QA unchanged.

| Experiment | Decision | Evidence and reason |
|---|---|---|
| Player | Keep | The original2008 artwork starts in its real mobile bounds, expands, contracts while metadata assembles, and returns into the same personal screen. It remains the eye's anchor instead of disappearing at three layout cuts. No full-white reset. |
| Discovery | Keep; strongest improvement | A real history-topic row detaches while the Ritan cover becomes the persistent programme identity. That cover remains as an earlier route marker while the journey branches into Stochastic's programme and real episode page. This preserves different programme/episode identities and makes browsing spatially understandable. |
| Critical | Reject from final | The web-to-phone experiment is viable but its short transition compresses too many changes: frame, artwork, transport, text and identity. The phone-to-brand exit adds complexity rather than explaining personal fit. Sixth's quiet comparison communicates the point more directly. Final Hero delegates the whole Critical chapter to Sixth. |

## Preservation and scope

- 936 baseline files snapshotted before implementation. Only the composition registry is intentionally changed, by adding Hero and a separate experimental composition; existing registrations remain intact.
- 55 of64 shots delegate directly to Sixth. Player includes its existing return shot as a necessary exit; outside Player21.917–33.900s and Discovery46.367–59.267s, visual source code delegates to Sixth. Timings remain the original rounded30fps boundaries.
- The two changed intervals occupy about25s, or13.5% of runtime. Thus “95% untouched” is interpreted as preservation of the finished film's system/content, not a literal frame percentage. No retiming, new content, new SFX, caption changes or soundtrack edits.
- Show Notes, Comments, History, Daqing, the complete Critical chapter and ending are preserved. The displayed Stochastic episode is not claimed to be the remembered Daqing episode.

## Resolution

New webpage/row fragments use600px captures at650px maximum:1.0833x. Original artwork uses1440px2008 artwork,1400pxRitan cover and3000pxStochastic programme cover. Mobile source remains1206×2622px. Every Hero raster checks its real crop and display factor on every rendered frame, with UI<=1.25x and artwork<=1.5x. Masks do not relax the budget.

The original `discovery-stochastic.jpg` is episode artwork, not the blue programme cover. The Hero programme cover comes from the image URL already observed in Sixth's authentic programme source, with `@small` removed. Dimensions and SHA are recorded in `hero-source-record.json`; Sixth assets are untouched.

## QA and review files

- `hero-player/discovery/critical-strip.jpg` and matching short previews show the actual final encode.
- `hero-*-comparison.mp4`: Sixth on the left, final Hero on the right. The Critical comparison is intentionally unchanged.
- `hero-critical-experiment.mp4` and its strip show the rejected experiment; `LittleUniverseReviewHeroExperiments` retains editable experimental code.
- Eight30fps frame-by-frame strips cover expansion, contraction, page reveal, phone return, topic-row extraction, catalogue browsing, programme branching and episode entry.
- `hero-native/` contains37 native1920×1080 samples, including transition boundaries and unchanged Critical samples. Native samples are the sharpness evidence; reduced strips are motion/navigation evidence.
- Visual review caught a clipped-page wrapper, programme-versus-episode artwork mismatch, duplicate cover edges and a brief handoff dim. The phone geometry now matches Sixth's border-box/object-fit layout, and its existing RMS waveform travels into the return rather than appearing abruptly. These were corrected before final acceptance. Caption/narration anchors and the Daqing entry remain original.
- Lint/typecheck and full video/audio decode pass. AAC payload MD5 matches Sixth exactly: `61a3997ba976d6b4e6f483cd1539764b`. `captions-hero.srt` is a byte-for-byte copy of frozen `captions-sixth.srt`. Final hashes and preservation results are in `hero-technical-qa.json` and `hero-preservation-result.json`.

Sound is preserved, not redesigned or newly auditioned. Technical audio identity does not constitute a new auditory judgement. The claim that the voice already works comes from the accepted Sixth state and user direction.

## Rebuild

`npm run lint`

`npx remotion render LittleUniverseReviewHero out/little-universe-review-hero-edit.mp4 --codec=h264 --crf=16 --image-format=png --concurrency=4 --log=error`

`python scripts/native_qa_hero.py`

`python scripts/qa_hero.py`

To rebuild the rejected Critical clip, render `LittleUniverseReviewHeroExperiments` with `--frames=4652-5058` to `analysis/hero-critical-experiment.mp4`. Do not run Sixth builders or QA scripts for this experiment; some rewrite frozen files.

Final master:184.042667s,5520 video frames,29,611,066bytes. SHA-256:`f40f9eaa8c89e0fe385bf3cd086e6e5ac3dccc8579da628c34074d53b8358793`. Browser comparisons were played at1x and reached ended:true without media errors; this is playback evidence, not a new auditory review.
