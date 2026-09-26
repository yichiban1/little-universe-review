import {loadFont} from '@remotion/fonts';
import {staticFile} from 'remotion';

// Latin editorial text only; captured Chinese UI pixels remain untouched.
loadFont({family:'Inter',url:staticFile('fonts/inter-latin-wght-normal.woff2'),weight:'100 900'});
loadFont({family:'Inter Tight',url:staticFile('fonts/inter-tight-latin-wght-normal.woff2'),weight:'100 900'});
