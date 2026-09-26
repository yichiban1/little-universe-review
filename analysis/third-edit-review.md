# Third edit review

## Changes made after visual inspection

- Replaced paragraph fractions with 58 named shots anchored to actual narrated words. Individual shot durations range from 1.07 to 5.75 seconds; the source timeline has no gaps.
- Removed stock commuter imagery and detached cover collages. Covers stay in the actual feed/search promotional images or the supplied player.
- Rebuilt the notes passage around the supplied episode page. The Olympics photograph enlarges from its location in the notes; it contracts as the DVD photograph expands; that photograph returns to the phone. Two additional photographs come from the same official published episode.
- Reviewed early renders as contact sheets and 6 fps transition samples. Revised image easing, separated photo and interface timing, enlarged the outline scroll, and removed overlapping explanatory labels.
- Opened Remotion Studio, checked loaded images at selected frames, played the notes passage muted, and checked the real 02:33 input-box crop. The comments are presented as separate listener memories, not falsely timestamped replies.
- Replaced the synthetic waveform with measured narration RMS. Replaced procedural audio with recorded public-domain/CC0 effects and a CC0 music recording. Eight sound events follow selected actions; music volume varies smoothly by passage.
- Rewrote the English narration and generated two voice samples. The delivered version uses one continuous Andrew master; second-edit source, audio and video are preserved.
- Inspected the first full export, then raised the dark sticker-image brightness and removed the final explanatory text overlay. Rendered the full film again and regenerated review artifacts from the final file.
- Kept “Little Universe”, “X Doctor” and “Show Notes” together at caption boundaries. Extended the last picture through the final composition frame so frame rounding does not produce a dark flash at the end.

## Encode checks

- Video: H.264, 1920×1080, 30 fps. Encoded container duration: 2:59.03; visual composition: 5369 frames (2:58.97).
- Audio: AAC, 48 kHz, stereo. Full-decode volume check: mean -22.8 dBFS; sample peak -5.3 dBFS. No sample clipping detected. This check does not establish perceived voice balance or true peak.
- `npm run lint` passed (ESLint and TypeScript). The complete MP4 decoded successfully during extraction and audio checks.

## Review artifacts

`third-edit-sheet-1.jpg` through `third-edit-sheet-4.jpg` sample the final MP4 approximately every two seconds. Six `third-motion-*.mp4` files are extracted from that same encode: opening, player, discovery, notes, comments and ending. Final-resolution frames are saved as `third-final-*.jpg`.

## Limits of this review

The interface motion is an editorial reconstruction from screenshots, not a live screen recording. The discovery material is official promotional imagery with older visible UI; it is not a capture of the user's current feed. The initial search field is an editorial graphic. Asset provenance and reuse limits are in `story/sources.md`.

The visual progression and frame composition were inspected. Audio was checked numerically for duration and peak level, but this environment could not reliably listen to or compare the voice and music. The two opening voice samples remain available for human listening. A successful render does not establish natural pronunciation, musical taste or subjective sound quality.
