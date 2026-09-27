# Resolution and scope audit

The frozen Hero raster helpers, real crop checks, phone border/mask geometry and
source dimensions are retained. `hero-polish-source-contract.json` records the
13 actual image dimension checks and normalized film-wrapper identity.

| Use | Source width | Maximum display width | Effective source scale |
|---|---:|---:|---:|
| 2008 travelling artwork | 1440 | 810 | 0.5625x |
| 2008 metadata excerpt | 600 | 650 | 1.0833x |
| Topic, extracted row and programme/episode page excerpts | 600 | 650 | 1.0833x |
| Ritan cover | 1400 | 390 | 0.2786x |
| Stochastic programme cover | 3000 | 390 | 0.1300x |
| Mobile player | 1206 | 468 outer phone | <0.389x |

UI <=1.25x and artwork <=1.5x remain enforced on every rendered frame. No new
source, sharpening, upscaling or blur. Other shots inherit the accepted Hero/Sixth
guards and visual content.

26 native 1920×1080 encoded frames are in `hero-polish-native/`, extracted from
the final encode. Reduced strips are timing/composition evidence, not sharpness
evidence. 20 separately rendered protected frames, including both entry/exit
boundaries and later chapters, are PNG-byte-identical to the frozen Hero source.
Those checks validate source-render identity; the full H.264 file is a new encode
and is not asserted to have identical compressed video packets.

The original checkout and original outputs pass exact SHA-256 preservation for
929 files. Text newline differences in the new Git worktree are normalized only
for cross-checkout comparison; exact original-file hashes are checked separately.
