# Opening Hero: review and decision

**Decision: retain Hero Polish as the submission version.** Opening Hero remains an isolated experiment on `opening-hero`, composition `LittleUniverseReviewOpeningHero`. No existing composition was replaced. Base `bf85a11`.

## Editorial acceptance
| Criterion | Result |
|---|---|
| One journey / inherited objects | Improved: programme cover survives the video and search geometry; distinct episode cover lands inside the exact supplied player crop. |
| Same object across states | Yes: one programme-cover element, then one 2008-cover element; the phone persists through the surrounding surfaces. |
| Real search result | Not met literally. Repository has no X Doctor search screenshot. The editorial query opens an authentic programme header. This is documented, not presented as a captured app result. No Google, stock or generated material added. |
| Product identity | Clear title and original icon at the original title interval. |
| Promise instead of summary | Improved: Notes photographs, a comment-body crop and app-wide 128h total appear as glimpses around the phone. No new explanatory feature cards. |
| Intentional motion | Improved cover/phone handoffs and one anchored rail. The first identity hold and video beat still carry preview-shot characteristics. |
| Earned title | Partial. The collection is related spatially, but the large icon ultimately takes over through a fade; this does not yet read as a signature transformation. |
| Clearly more memorable first 15 seconds | Not established strongly enough to recommend replacement. Continuity alone is insufficient for the user's promotion gate. |
| Rest unchanged | Yes: frame 577 onwards invokes only the original mounted HeroPolishFilm. |

## Playback and evidence
Both the comparison and the standalone experiment played at 1x to ended=true, without media error, in the in-app browser. Playback-end JSON records and a browser screenshot are saved. Browser snapshots were inspected during playback; all five transition windows have every-frame contact sheets. This is visual review with sampled live observations and frame strips, not a claim of continuous human sight or an auditory quality sign-off. Audio was not redesigned; its encoded payload was checked.

Files:
- opening-hero-baseline.mp4: freshly rendered frozen Hero Polish frames 0–576.
- opening-hero-preview.mp4: experiment at identical frame range.
- opening-hero-comparison.mp4: Hero Polish left / experiment right; baseline audio once.
- opening-hero-strip.jpg: 0.5-second overview.
- opening-hero-framebyframe-{xdoctor-search,search-2008,2008-phone,phone-surfaces,title-reveal}.jpg: every frame, no skipped transition frames.
- opening-hero-native/: 17 final-source 1920x1080 PNG samples; reduced strips do not prove sharpness.

## Preservation and resolution
- npm run lint and git diff --check passed.
- Full runtime stays 5520 frames / 184 seconds. Boundary is frame 577 / 19.233 seconds, derived from rounded original 19222ms chapter start.
- Both opening encodes are 1920x1080, 30fps, 577 video frames. MP4 duration 19.285333s includes AAC padding; the video range is 19.233333s.
- Baseline and preview AAC payload MD5 are identical: 7789e40b9691a4fb08c65639b229d61d. Narration, Andrew voice, music and all original SFX code/files are frozen. No new SFX.
- All 1020 original tracked files match the original worktree, allowing checkout newline differences, except the two additive lines in Composition.tsx. 1021 original hashes recorded including the accepted external master.
- Original full master still has SHA256 bb3a5fa55f3733211cd3b2b0e556b7ef41f749c29b464b92947416e773bf46a0.
- 14 native source frames at/after the handoff are PNG-byte-identical: 577,578,657,1020,1391,1778,1900,2500,3000,3600,4200,4652,5058,5519. Structural delegation protects all later frames; the samples do not assert compressed packet identity for a future full encode.
- Opening caption data and exact caption styles are copied from the frozen caption layer, only above the opening visual overlay. After frame 577 the original caption layer alone is visible.
- UI maximum 650/600=1.083333x; cover maximum 650/1440=.451389x; video thumbnail maximum 1280/1280=1x; player maximum 426/1206=.353234x. Notes 440/1206=.364842x, comments 475/1206=.393864x, history 490/1100=.445455x, icon 535/1200=.445833x. Actual crop bounds and scale are guarded on every rendered frame. All limits <=1.25x UI / <=1.5x imagery.
- No sharpening, AI upscaling, fake blur, new asset, font, colour or audio source.

## Rebuild
From this isolated worktree:
```
npm run lint
node scripts/render_opening_hero.cjs
node scripts/render_opening_hero.cjs --preserve
node scripts/render_opening_hero.cjs --stills
python -X utf8 scripts/qa_opening_hero.py
```
The full experimental composition is available in Studio, but only the requested opening A/B clips were exported. Keep Hero Polish for submission. Branch is local; no push or PR.
