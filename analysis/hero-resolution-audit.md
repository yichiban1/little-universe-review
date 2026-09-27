# Hero resolution contract

Final retained experiments use the following analytic maximum source scales. Every rendered frame also executes the raster/crop guard. Actual source dimensions have been checked against image files in `hero-source-contract.json`.

| Source/use | Source pixels | Maximum display width | Scale | Contract |
|---|---:|---:|---:|---|
| 2008 episode artwork, travelling object |1440×1440|810|0.5625x|Artwork<=1.5x |
| Personal mobile player, masked surface |1206×2622|468 outer phone; cover fit within border|<0.389x|UI<=1.25x |
| 2008 metadata excerpt |600×562, crop600×390|650|1.0833x|UI<=1.25x; crop in bounds |
| Ritan topic and extracted row |600×900, row600×92|650|1.0833x|UI<=1.25x; crop in bounds |
| Ritan programme excerpt |600×900, crop600×722 at y178|650|1.0833x|UI<=1.25x; crop in bounds |
| Sound programme excerpt |600×900, crop600×620 at y180|650|1.0833x|UI<=1.25x; crop in bounds |
| Stochastic programme excerpt |600×900, crop600×720 at y180|650|1.0833x|UI<=1.25x; crop in bounds |
| Stochastic episode page |600×900|650|1.0833x|UI<=1.25x |
| Ritan original programme cover |1400×1400|390|0.2786x|Artwork<=1.5x |
| Stochastic original programme cover |3000×3000|390|0.1300x|Artwork<=1.5x |

The other55 shots preserve SixthShot and its existing guards. Maximum inherited UI scale remains1.2414x; the protected archival Olympics source remains at its previously accepted1.5x limit. No sharpening, artificial enlargement or blur conceals missing source pixels.

The rejected Critical experiment uses the authentic1888×69 transport at1920px maximum (1.01695x),650px webpage excerpts and original1440px artwork; it is excluded for editorial reasons, not because of a failed resolution gate.

Native1920×1080 encoded samples are retained in `hero-native/`. Small contact/motion strips demonstrate movement but are not pixel-quality acceptance evidence.
