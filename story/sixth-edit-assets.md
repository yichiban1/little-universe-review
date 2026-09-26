# Sixth acquisition and source treatment

This is a mastering branch of Fifth. Personal phone, listening history, app screenshots, Inter fonts, continuous Andrew voice, captions, music and recorded sound remain the preserved originals.

## Revisited public sources

The X Doctor [programme](https://www.xiaoyuzhoufm.com/podcast/62d517139e6a635a41fd1002), [2008 episode, Notes, discussion and active player](https://www.xiaoyuzhoufm.com/episode/666fd8d7c26e396a3656f1e0), Ritan [topic](https://www.xiaoyuzhoufm.com/podcast-topic/654378487f6b61e917247e10), [programme](https://www.xiaoyuzhoufm.com/podcast/5e280faa418a84a0461f9ad8) and [episode](https://www.xiaoyuzhoufm.com/episode/67d6a8ff0766616acd4f4ceb), Stochastic [programme](https://www.xiaoyuzhoufm.com/podcast/5e7cc741418a84a046b0c2bd) and [episode](https://www.xiaoyuzhoufm.com/episode/6a1fa78c57efa503e137cce3), and Sound [programme](https://www.xiaoyuzhoufm.com/podcast/5e2831ed418a84a046231c00) were revisited through CUA.

The available browser supports viewport width/height, but no DPR override. A 1920×1080 viewport and browser zoom shortcuts were tried. The shortcuts did not change the 600 CSS pixel main column. Neither a large viewport nor the reported DPR 1.5 produced a 1400–2000 pixel content column. Consequently the accepted page sources remain 600 pixel crops of ordinary viewport captures, displayed at 620–650 pixels. Full-page and clipped screenshots exhibited a resampling/coordinate defect; those research captures are rejected, not final assets. Accepted viewport files and observed page metadata are recorded in `analysis/sixth-research/acquisition.json`.

The student comment is an offline crop of the visible real comment body, with margin, from `student-viewport.png`. Names and reply text are excluded. Its displayed width is 635 pixels. The Chengdu comment retains the supplied redacted mobile screenshot at 850 pixels. Large labels are editorial vector type, not recreated comments.

The active player was actually started on the same 2008 episode and paused after capture. Its source transport strip is 1888×69 pixels and displays at 1920 pixels. The visible controls are 15 seconds back / pause / 30 seconds forward. The strip omits unrelated comment text and the scrollbar. Public web playback demonstrates availability, not the user's personal listening session.

## Original media, not enlarged thumbnails

| Sixth asset | Actual source file | Treatment |
|---|---|---|
| `xdoctor-cover-sixth.jpg` | 1440×1440 | Observed `FpiG4q0qhaLuTRJbUipPcGCn8jkc.jpg@small` image URL, with CDN thumbnail transform removed to retrieve its original. Same programme artwork. |
| `xdoctor-episode-art-sixth.png` | 1440×1440 | Observed `Fi3BhNFKCMtkqf8VcSB7jAUugFmN.png@small`, original retrieved without thumbnail transform. Same 2008 episode. |
| `notes-dvd-sixth.png` | 1920×1257 | Exact original URL exposed by the Notes image DOM: `https://image.xyzcdn.net/lp-aiFgbBF31BNpMzUeT7ZxmTV-I.png`. |
| `notes-beijing-sixth.png` | 550×366 | Exact Notes DOM original: `https://image.xyzcdn.net/FrMysCziH2A9voIykXFNniAJ5VDf.png`. The old 1087×513 mobile derivative already enlarged and cropped this photograph. Sixth uses the actual original, with sky restored; maximum 825×549. |

These are the same editorial sources, not unrelated new imagery. Downloads are recorded in `analysis/sixth-research/original-downloads.json`. No AI upscaling, sharpening or cosmetic texture is used. The low resolution stadium/dorm originals remain 500×333 and 300×200; their displays are reduced to 500×333 and 330×220.

## Rebuild

1. `python scripts/build_sixth.py`
2. `python scripts/audit_sixth.py`
3. `npm run lint`
4. `npx remotion render LittleUniverseReviewSixth out/little-universe-review-sixth-edit.mp4 --codec=h264 --crf=16 --image-format=png --concurrency=4`
5. `python scripts/native_qa_sixth.py`
6. `python scripts/qa_sixth.py`

The audit enumerates every rendered raster use. Runtime guards also reject an over-budget animated value on any frame. Sixth references Fifth timing, words, captions and sound intentionally; it does not regenerate or overwrite them. The fifth/shared preservation manifest contains 155 files.
