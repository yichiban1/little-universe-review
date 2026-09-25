import {Composition} from 'remotion';
import {Film,totalFrames} from './Film';
export const MyComposition=()=> <Composition id="LittleUniverseReview" component={Film} durationInFrames={totalFrames} fps={30} width={1920} height={1080}/>;
