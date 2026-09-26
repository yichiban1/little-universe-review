import {Composition} from 'remotion';
import {Film,totalFrames} from './Film';
import {ThirdFilm,thirdTotalFrames} from './ThirdFilm';
import {FourthFilm,fourthTotalFrames} from './FourthFilm';
import {FifthFilm,fifthTotalFrames} from './FifthFilm';
export const MyComposition=()=> <>
 <Composition id="LittleUniverseReview" component={Film} durationInFrames={totalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewThird" component={ThirdFilm} durationInFrames={thirdTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewFourth" component={FourthFilm} durationInFrames={fourthTotalFrames} fps={30} width={1920} height={1080}/>
 <Composition id="LittleUniverseReviewFifth" component={FifthFilm} durationInFrames={fifthTotalFrames} fps={30} width={1920} height={1080}/>
 </>;
