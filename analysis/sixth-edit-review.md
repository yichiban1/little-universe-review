# Sixth resolution-first mastering review

## Master

- Independent `SixthEdit.tsx` / `SixthFilm.tsx` composition. 5520 frames, 30 fps, 1920×1080, 184.00 seconds of composition time. Same Fifth shot timings, continuous Andrew narration, Inter typography, captions, actual RMS waveform, recorded music and eight sound cues.
- H.264 CRF 16, PNG source frames. This reduces encode damage to type; it does not create missing source pixels.
- Fifth and shared inputs have a 155-file SHA-256 preservation manifest. Existing Fifth outputs and source are preserved. The previous handoff is separately saved before updating the current handoff.

## Resolution findings and corrections

The Fifth audit covers 78 rendered raster uses in 64 shots: 39 SAFE, 8 BORDERLINE, 31 UNACCEPTABLE; eight UI/text uses above 2×. These counts include the inherited enlargement in the old Olympics mobile crop. The Sixth audit covers 84 uses: 82 SAFE, two BORDERLINE archival-photo uses, zero UNACCEPTABLE; zero UI/text above 2×. Maximum UI/text enlargement is 1.2414×. Every animated raster helper also checks its budget at render time.

| Passage | Fifth problem | Sixth treatment |
|---|---|---|
| Player title / Notes entry | 572px →1790 /1720 | Same episode page at 620–650px, readable vector editorial context. |
| Player artwork | 930px mobile crop →2020 | Same episode's real 1440px artwork, plus the personal player screen. |
| Topic / catalogue | 572px →945–1920 | Revisited original page content, 600px crops →650; no giant raster background. |
| Widgets / transport | 1242 /1206 →1990 /1920 | Controls at 1500 /1490, within the pixel budget. |
| Student / Chengdu | 510 →1780 and1130 →1920 | Real student text533 →635; supplied redacted Chengdu crop1130 →850, with vector labels. |
| History total | 355px number crop →1520 | Clean full original1100 →1050, with vector “128 h /27 m /TOTAL LISTENING”. |
| Creator sticker | 550px →830 | Actual sticker at550px, with separate vector “100 h /WITH ONE CREATOR”. No sticker recreation. |
| Web availability | 572px page1250;974px strip1920 | Same episode650px; actual active1888px strip1920, then personal mobile preference. |
| Notes photographs | Stadium/dorm cover crop2.31 /3.85×; mobile Olympic photo hid an earlier enlargement | Stadium500px, dorm330px. Actual Olympic550×366 →825×549 at most. Original DVD1920×1257 supports the retained large expansion/return. |

The browser had a 1920×1080 viewport, but zoom shortcuts did not enlarge its fixed 600px main column and no DPR override was available. Reacquisition therefore uses real viewport captures and smaller composition. Full-page/clip capture defects were found during original-size inspection and rejected. Source records are in `story/sixth-edit-assets.md`.

## Editorial continuity

Three formerly sparse Player/Listening observations now carry the same personal episode evidence. The final waveform-only hold also returns to the genuine player. Only Daqing and the first-person critical statement remain independent quiet type moments. No unrelated episode is introduced to add variety.

Notes retains the established launch → Olympics expansion → DVD change → larger DVD hold → contraction into Notes choreography and durations. Its Olympic endpoint is smaller because the actual archival original has fewer pixels. The DVD endpoint/return remain large. Stadium/dorm are shown near native size instead of portrait crops. These changes preserve the editorial cause of the motion.

Comments stay personal time02:33 → input → student memory → Chengdu memory → return to listening. Public listener memories are not assigned the user's timestamp. Editorial labels carry the emphasis; the real comment text remains evidence rather than a recreated quote.

History separates total128h27 from100h with one creator. The critical review retains English listening elsewhere, real web availability, mobile preference and Chinese podcast identity. Ending preserves the natural final sentence and5.72-second identity shot. No narration stretching or new rests were added.

## Native QA

All 64 shot representatives were inspected as actual encoded 1920×1080 PNGs at original size. Small contact sheets serve navigation; they are not the sharpness acceptance gate. Native review found two mini-player crops with displaced source origins; the builder was corrected, explicit crop-bound checks were added to both runtime and audit, and the final master was rendered again. The corrected `listen-mini-detail` and `notes-player-return` frames now retain the complete icon, episode title and playback time.

Source reading targets pass within their available resolution: the personal player transport, Notes outline, student memory, Chengdu memory, history totals and actual creator sticker remain legible. Website grey metadata has the site's intrinsic low contrast; large editorial reading targets are clean vector type. The archival Olympic photograph is the only repeated borderline source, at exactly 1.5×. Notes expansion, DVD hold and contraction remain coherent in the motion strip. The film retains two quiet editorial moments and the personal critical judgement.

The final master is 28,583,239 bytes, H.264 High / yuv420p, 1920×1080 /30 fps, with AAC 48 kHz stereo. Container duration is 184.042667 seconds. The complete video decodes for sheet/clip generation and all native frame extractions; lint/typecheck and the source-resolution gate pass. All 155 preservation hashes match. Final mean audio level is -23.0 dBFS and sample peak -6.0 dBFS. Fifth and Sixth AAC payload MD5 values are identical (`61a3997ba976d6b4e6f483cd1539764b`), confirming the soundtrack is unchanged. This is a technical audio check; auditory naturalness and balance were not heard in this environment.

The actual final master was played from the beginning at 1× without seeking, reaching `ended: true` at184.042667 seconds, with no media error. `analysis/sixth-research/playback-final.json` records the final SHA-256 in the loaded media URL; `playback-ended.png` shows the end state. An initial cached playback was discarded. The review URL now carries the master hash to prevent confusion between renders.

All64 shots were subsequently paused in the actual final video using visible player buttons. Every recorded time matches its shot target within0.01 seconds; all pauses are1920×1080 video and error-free. Records: `analysis/sixth-research/browser-pauses.json`; screenshots: `analysis/sixth-browser-pauses/`. The local QA server supports byte-range requests for reliable seeking (`python scripts/serve_sixth_qa.py`, port8817). Browser proof screenshots clip the host's right edge; original1920×1080 encoded PNGs in `analysis/sixth-native/` provide the complete100% pixel inspection. Browser proof is not substituted for these native frames.

Intrinsic limits remain: the supplied personal captures and old archival photographs are not newly recorded mobile video. Near-native presentation preserves available detail; vector annotations carry major reading targets. The Olympic original remains a550px historical photograph, explicitly held to1.5×. There is no claim that every piece of tiny captured UI copy becomes a large reading target.

## Deliverables

- `out/little-universe-review-sixth-edit.mp4`, plus matching `out/captions-sixth.srt`.
- Four `sixth-edit-sheet-*.jpg` contact sheets.
- Nine `sixth-motion-*.mp4` clips and strips, including all seven requested chapters.
- Every-shot native encoded PNGs and their timing manifest in `analysis/sixth-native/`.
- `sixth-resolution-audit.md`, `sixth-pixel-quality-audit.md`, this review, source records and Sixth build/audit/QA scripts.
