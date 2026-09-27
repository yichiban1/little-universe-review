import {Composition} from 'remotion';
import {Film,totalFrames} from './Film';
import {ThirdFilm,thirdTotalFrames} from './ThirdFilm';
import {FourthFilm,fourthTotalFrames} from './FourthFilm';
import {FifthFilm,fifthTotalFrames} from './FifthFilm';
import {SixthFilm,sixthTotalFrames} from './SixthFilm';
import {HeroFilm,heroTotalFrames} from './HeroFilm';
import {HeroPolishFilm,heroPolishTotalFrames} from './HeroPolishFilm';
import {OpeningHeroFilm} from './OpeningHeroFilm';
import {HeroExperimentFilm} from './HeroExperiments';
export const MyComposition=()=> <>
 <Composition id="LittleUniverseReview" component={Film} durationInFrames={totalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewThird" component={ThirdFilm} durationInFrames={thirdTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewFourth" component={FourthFilm} durationInFrames={fourthTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewFifth" component={FifthFilm} durationInFrames={fifthTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewSixth" component={SixthFilm} durationInFrames={sixthTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewHero" component={HeroFilm} durationInFrames={heroTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewHeroExperiments" component={HeroExperimentFilm} durationInFrames={heroTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewHeroPolish" component={HeroPolishFilm} durationInFrames={heroPolishTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewOpeningHero" component={OpeningHeroFilm} durationInFrames={heroPolishTotalFrames} fps={30} width={1920} height={1080}/>
 </>;

