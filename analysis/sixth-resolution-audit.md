# Fifth source-resolution audit

Audited 78 rendered raster instances in all 64 Fifth shots. {'SAFE': 39, 'BORDERLINE': 8, 'UNACCEPTABLE': 31}. UI/text above 2×: 8.

Actual crop accounts for `objectFit: cover`, explicit Crop boxes, WebPage viewport height, and Phone aspect ratio. Maxima conservatively evaluate all motion endpoints; hidden offscreen pixels do not excuse overscaling. Display bounds include the image before stage clipping. Unused inherited branches are excluded because they do not render. SAFE ≤1.25×; BORDERLINE >1.25–1.5×; UNACCEPTABLE >1.5×. SAFE is a sampling-budget result, not proof of intrinsic source sharpness.

| Shot / use | Source | Original px | Actual crop px | Display px (max) | Enlargement | UI/text | Gate |
|---|---|---:|---:|---:|---:|---|---|
| open-cover / WebPage | web-xdoctor-programme.png | 572 × 770 | 572 × 601.3 | 780.0 × 820.0 | 1.364× | yes | BORDERLINE |
| open-cover / Picture | xdoctor-cover.jpg | 300 × 300 | 300.0 × 300.0 | 440.0 × 440.0 | 1.467× | no / artwork-photo | BORDERLINE |
| open-video / Picture | xdoctor-video-thumbnail.jpg | 1280 × 720 | 1280.0 × 718.9 | 1460.0 × 820.0 | 1.141× | no / artwork-photo | SAFE |
| open-video / Picture | xdoctor-cover.jpg | 300 × 300 | 300.0 × 300.0 | 170.0 × 170.0 | 0.567× | no / artwork-photo | SAFE |
| open-search / Picture | xdoctor-video-thumbnail.jpg | 1280 × 720 | 1278.5 × 720.0 | 950.0 × 535.0 | 0.743× | no / artwork-photo | SAFE |
| open-result / WebPage | web-xdoctor-2008.png | 572 × 574 | 572 × 510.9 | 1310.0 × 1170.0 | 2.290× | yes | UNACCEPTABLE |
| open-player / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 521.0 × 1132.7 | 0.432× | yes | SAFE |
| open-notes / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 450.0 × 978.4 | 0.373× | yes | SAFE |
| open-notes / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 450.0 × 978.4 | 0.373× | yes | SAFE |
| open-comments / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 445.0 × 967.5 | 0.369× | yes | SAFE |
| open-comments / Phone | ui-comments-redacted.jpg | 1206 × 2622 | 1206 × 2622 | 445.0 × 967.5 | 0.369× | yes | SAFE |
| open-title / Picture | little-universe-icon.png | 1200 × 1200 | 1200.0 × 1200.0 | 535.0 × 535.0 | 0.446× | yes | SAFE |
| player-full / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 468.0 × 1017.5 | 0.388× | yes | SAFE |
| player-art / Crop | ui-player.jpg | 1206 × 2622 | 930.0 × 925.0 | 2020.0 × 2009.1 | 2.172× | yes | UNACCEPTABLE |
| player-title / Crop | web-xdoctor-2008.png | 572 × 574 | 572.0 × 103.0 | 1790.0 × 322.3 | 3.129× | yes | UNACCEPTABLE |
| player-return / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 486.7 × 1058.2 | 0.404× | yes | SAFE |
| player-timeline / Crop | ui-player.jpg | 1206 × 2622 | 1135.0 × 660.0 | 1580.0 × 918.8 | 1.392× | yes | BORDERLINE |
| player-rewind / Crop | ui-player.jpg | 1206 × 2622 | 1160.0 × 590.0 | 1640.0 × 834.1 | 1.414× | yes | BORDERLINE |
| feed-enter / Picture | official-home-subscriptions.png | 843 × 1322 | 843 × 1322 | 510.0 × 799.8 | 0.605× | yes | SAFE |
| feed-search / Picture | appstore-6.jpg | 1242 × 2208 | 1241.3 × 2208.0 | 800.0 × 1423.0 | 0.644× | yes | SAFE |
| feed-discover / WebPage | web-stochastic-programme.png | 572 × 770 | 572 × 566.9 | 1120.0 × 1110.0 | 1.958× | yes | UNACCEPTABLE |
| feed-select / WebPage | web-stochastic-episode.png | 572 × 579 | 572 × 566.9 | 1120.0 × 1110.0 | 1.958× | yes | UNACCEPTABLE |
| notes-enter / Crop | web-xdoctor-2008.png | 572 × 574 | 572.0 × 103.0 | 1720.0 × 309.7 | 3.007× | yes | UNACCEPTABLE |
| notes-open / Phone | ui-notes-text.jpg | 1206 × 2622 | 1206 × 2622 | 480.0 × 1043.6 | 0.398× | yes | SAFE |
| notes-outline / Crop | ui-notes-text.jpg | 1206 × 2622 | 1135.0 × 1420.0 | 1450.0 × 1814.1 | 1.278× | yes | BORDERLINE |
| notes-stadium / Picture | notes-stadium.png | 500 × 333 | 261.6 × 333.0 | 605.0 × 770.0 | 2.312× | no / artwork-photo | UNACCEPTABLE |
| notes-stadium / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 480.0 × 1043.6 | 0.398× | yes | SAFE |
| notes-dorm / Picture | notes-dorm.png | 300 × 200 | 157.1 × 200.0 | 605.0 × 770.0 | 3.850× | no / artwork-photo | UNACCEPTABLE |
| notes-dorm / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 480.0 × 1043.6 | 0.398× | yes | SAFE |
| notes-olympic / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 480.0 × 1043.6 | 0.398× | yes | SAFE |
| notes-olympic / Picture | notes-beijing.jpg | 1087 × 513; 550 × 366 origin; mobile crop already enlarged | 550.0 × 259.6 | 1320.0 × 623.0 | 2.400× | no / artwork-photo | UNACCEPTABLE |
| notes-dvd / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 380.0 × 826.2 | 0.315× | yes | SAFE |
| notes-dvd / Picture | notes-beijing.jpg | 1087 × 513; 550 × 366 origin; mobile crop already enlarged | 550.0 × 259.6 | 1320.0 × 623.0 | 2.400× | no / artwork-photo | UNACCEPTABLE |
| notes-dvd / Picture | notes-dvd.jpg | 1087 × 713 | 1086.4 × 713.0 | 1190.0 × 781.0 | 1.095× | no / artwork-photo | SAFE |
| notes-dvd-hold / Picture | notes-dvd.jpg | 1087 × 713 | 1085.9 × 713.0 | 1660.0 × 1090.0 | 1.529× | no / artwork-photo | UNACCEPTABLE |
| notes-return / Phone | ui-notes-photos.jpg | 1206 × 2622 | 1206 × 2622 | 400.0 × 869.7 | 0.332× | yes | SAFE |
| notes-return / Picture | notes-dvd.jpg | 1087 × 713 | 1085.9 × 713.0 | 1660.0 × 1090.0 | 1.529× | no / artwork-photo | UNACCEPTABLE |
| notes-outline-return / Phone | ui-notes-text.jpg | 1206 × 2622 | 1206 × 2622 | 475.0 × 1032.7 | 0.394× | yes | SAFE |
| notes-outline-return / Crop | ui-notes-text.jpg | 1206 × 2622 | 1135.0 × 800.0 | 620.0 × 437.0 | 0.546× | yes | SAFE |
| notes-player-return / Crop | ui-notes-text.jpg | 1206 × 2622 | 1206.0 × 265.0 | 1920.0 × 421.9 | 1.592× | yes | UNACCEPTABLE |
| comments-open / WebPage | web-xdoctor-discussion.png | 572 × 778 | 572 × 732.7 | 890.0 × 1140.0 | 1.556× | yes | UNACCEPTABLE |
| comments-open / Phone | ui-comments-redacted.jpg | 1206 × 2622 | 1206 × 2622 | 455.0 × 989.2 | 0.377× | yes | SAFE |
| comments-link / Phone | ui-comments-redacted.jpg | 1206 × 2622 | 1206 × 2622 | 480.0 × 1043.6 | 0.398× | yes | SAFE |
| comments-link / Crop | ui-comments-redacted.jpg | 1206 × 2622 | 1155.0 × 330.0 | 690.0 × 197.1 | 0.597× | yes | SAFE |
| comments-first / Crop | web-xdoctor-discussion.png | 572 × 778 | 510.0 × 95.0 | 1780.0 × 331.6 | 3.490× | yes | UNACCEPTABLE |
| comments-second / Crop | ui-comments-redacted.jpg | 1206 × 2622 | 1130.0 × 860.0 | 1920.0 × 1461.2 | 1.699× | yes | UNACCEPTABLE |
| comments-return / Phone | ui-comments-redacted.jpg | 1206 × 2622 | 1206 × 2622 | 445.0 × 967.5 | 0.369× | yes | SAFE |
| comments-return / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 445.0 × 967.5 | 0.369× | yes | SAFE |
| history-hours / Picture | ui-listening-hours.jpg | 1100 × 440 | 1100.0 × 440.0 | 1920.0 × 768.0 | 1.746× | yes | UNACCEPTABLE |
| history-stickers / Picture | ui-stickers.jpg | 1135 × 1560 | 1134.5 × 1560.0 | 640.0 × 880.0 | 0.564× | yes | SAFE |
| history-100 / Crop | ui-stickers.jpg | 1135 × 1560 | 550.0 × 720.0 | 830.0 × 1086.5 | 1.509× | yes | UNACCEPTABLE |
| history-return / Picture | ui-listening-hours.jpg | 1100 × 440 | 1100.0 × 440.0 | 1050.0 × 420.0 | 0.955× | yes | SAFE |
| history-return / Picture | ui-stickers.jpg | 1135 × 1560 | 1134.5 × 1560.0 | 520.0 × 715.0 | 0.458× | yes | SAFE |
| end-notes / Picture | notes-dvd.jpg | 1087 × 713 | 1086.5 × 713.0 | 1920.0 × 1260.0 | 1.767× | no / artwork-photo | UNACCEPTABLE |
| end-xdoctor / Picture | xdoctor-cover.jpg | 300 × 300 | 300.0 × 300.0 | 550.0 × 550.0 | 1.833× | no / artwork-photo | UNACCEPTABLE |
| end-history / Picture | ui-listening-hours.jpg | 1100 × 440 | 1100.0 × 440.0 | 1920.0 × 768.0 | 1.746× | yes | UNACCEPTABLE |
| end-icon / Picture | little-universe-icon.png | 1200 × 1200 | 1200.0 × 1200.0 | 340.0 × 340.0 | 0.283× | yes | SAFE |
| end-icon / Picture | official-wordmark-fourth.png | 1305 × 352 | 1305 × 352 | 411.5 × 111.0 | 0.315× | yes | SAFE |
| feed-topic / WebPage | web-ritan-topic.png | 572 × 775 | 572 × 321.8 | 1920.0 × 1080.0 | 3.357× | yes | UNACCEPTABLE |
| feed-programme / WebPage | web-ritan-programme.png | 572 × 770 | 572 × 702.1 | 945.0 × 1160.0 | 1.652× | yes | UNACCEPTABLE |
| feed-programme / WebPage | web-sound-programme.png | 572 × 770 | 572 × 702.1 | 945.0 × 1160.0 | 1.652× | yes | UNACCEPTABLE |
| listen-widgets / Picture | appstore-1.jpg | 1242 × 2208 | 1242 × 2208 | 610.0 × 1084.4 | 0.491× | yes | SAFE |
| listen-controls / Crop | appstore-1.jpg | 1242 × 2208 | 1242.0 × 570.0 | 1990.0 × 913.3 | 1.602× | yes | UNACCEPTABLE |
| listen-lock / Picture | appstore-7.jpg | 1242 × 2208 | 1242 × 2208 | 759.9 × 1351.0 | 0.612× | yes | SAFE |
| listen-mini / Phone | ui-notes-text.jpg | 1206 × 2622 | 1206 × 2622 | 485.0 × 1054.5 | 0.402× | yes | SAFE |
| listen-mini-detail / Crop | ui-notes-text.jpg | 1206 × 2622 | 1206.0 × 265.0 | 1920.0 × 421.9 | 1.592× | yes | UNACCEPTABLE |
| listen-back / Crop | ui-player.jpg | 1206 × 2622 | 1160.0 × 590.0 | 1570.0 × 798.5 | 1.353× | yes | BORDERLINE |
| comments-feature / Picture | appstore-5.jpg | 1242 × 2208 | 1242 × 2208 | 655.0 × 1164.4 | 0.527× | yes | SAFE |
| comments-context / WebPage | web-xdoctor-2008.png | 572 × 574 | 572 × 574 | 790.0 × 1130.0 | 1.381× | yes | BORDERLINE |
| comments-context / Crop | ui-player.jpg | 1206 × 2622 | 1130.0 × 690.0 | 1100.0 × 671.7 | 0.974× | yes | SAFE |
| end-shows / WebPage | web-ritan-episode.png | 572 × 544 | 572 × 544 | 945.0 × 1180.0 | 1.652× | yes | UNACCEPTABLE |
| end-shows / WebPage | web-stochastic-programme.png | 572 × 770 | 572 × 714.2 | 945.0 × 1180.0 | 1.652× | yes | UNACCEPTABLE |
| end-comments / Crop | ui-comments-redacted.jpg | 1206 × 2622 | 1130.0 × 860.0 | 1460.0 × 1111.2 | 1.292× | yes | BORDERLINE |
| history-emphasis / Crop | ui-listening-hours.jpg | 1100 × 440 | 355.0 × 170.0 | 1520.0 × 727.9 | 4.282× | yes | UNACCEPTABLE |
| critical-web / WebPage | web-xdoctor-playing-page-fifth.png | 572 × 562 | 572 × 562 | 1250.0 × 1240.0 | 2.185× | yes | UNACCEPTABLE |
| critical-web / Crop | web-xdoctor-playing-controls-fifth.png | 974 × 69 | 974.0 × 69.0 | 1920.0 × 136.0 | 1.971× | yes | UNACCEPTABLE |
| critical-phone / Phone | ui-player.jpg | 1206 × 2622 | 1206 × 2622 | 470.0 × 1021.8 | 0.390× | yes | SAFE |
| critical-fit / Picture | little-universe-icon.png | 1200 × 1200 | 1200.0 × 1200.0 | 340.0 × 340.0 | 0.283× | yes | SAFE |
