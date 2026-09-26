"""Anchor every third-edit shot to the first voiced word of a phrase."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
words = json.loads((ROOT/'src/words-third.json').read_text(encoding='utf-8'))
timing = json.loads((ROOT/'src/timing-third.json').read_text(encoding='utf-8'))

# Phrase, id, visual. The sequence follows the voice, rather than dividing
# paragraphs into an equal number of template shots.
spec = [
 ('I downloaded','open-cover','opening'),
 ("I'd watched",'open-video','opening'),
 ('searched the name','open-search','opening'),
 ('I opened an episode','open-result','opening'),
 ('pressed play','open-player','opening'),
 ('the notes, photos','open-notes','opening'),
 ('people talking','open-comments','opening'),
 ('Let me show you','open-title','opening'),
 ('The player is pretty plain','player-full','player'),
 ('The artwork is huge','player-art','player'),
 ('episode title','player-title','player'),
 ('This is the screen','player-return','player'),
 ("When I'm outside",'player-pocket','player'),
 ('If I miss something','player-timeline','player'),
 ('fifteen-second rewind','player-rewind','player'),
 ('I probably use','player-tap-hold','player'),
 ('After X Doctor','feed-enter','discovery'),
 ("I'd finish an episode",'feed-search','discovery'),
 ('The discovery page','feed-discover','discovery'),
 ('but I still choose','feed-select','discovery'),
 ('One episode mentioned Daqing','feed-daqing','discovery'),
 ("I wasn't looking",'feed-hold','discovery'),
 ('That wandering works','listen-player','listening'),
 ('A conversation can','listen-wave','listening'),
 ('Sometimes I catch','listen-rewind','listening'),
 ("Here's where the 2008",'notes-enter','notes'),
 ('I tap into its Show Notes','notes-open','notes'),
 ("First there's",'notes-outline','notes'),
 ('Then the notes move','notes-stadium','notes'),
 ('into photographs','notes-dorm','notes'),
 ("There's an image",'notes-olympic','notes'),
 ('and a photo of a DVD shop','notes-dvd','notes'),
 ('When someone talks','notes-dvd-hold','notes'),
 ('I like being able','notes-return','notes'),
 ('A long episode','notes-outline-return','notes'),
 ('instead of asking','notes-player-return','notes'),
 ("And the conversation",'comments-enter','comments'),
 ('two minutes thirty-three','comments-time','comments'),
 ('I can open the discussion','comments-open','comments'),
 ('comment box keeps','comments-link','comments'),
 ('one listener writes','comments-first','comments'),
 ('Another remembers','comments-second','comments'),
 ('I read a few','comments-return','comments'),
 ('and hear the episode differently','comments-player','comments'),
 ("That's a small interaction",'comments-hold','comments'),
 ('My profile says','history-hours','history'),
 ('There are stickers too','history-stickers','history'),
 ('This one marks','history-100','history'),
 ('You can put it','history-board','history'),
 ("I wouldn't open",'history-return','history'),
 ('I still use other apps','end-feed','ending'),
 ('Little Universe makes','end-app','ending'),
 ('and for how often','end-notes','ending'),
 ('That first X Doctor','end-xdoctor','ending'),
 ('but now there are other shows','end-journey','ending'),
 ('saved moments','end-saved','ending'),
 ('a lot of listening history','end-history','ending'),
 ('When someone sends','end-icon','ending'),
]

speech = ' '.join(w['text'] for w in words)
starts = []
cursor = 0
for word in words:
    starts.append(cursor)
    cursor += len(word['text'])+1

shots = []
search_from = 0
for phrase, shot_id, chapter in spec:
    pos = speech.lower().find(phrase.lower(), search_from)
    if pos < 0:
        raise RuntimeError(f'Missing phrase after {search_from}: {phrase}')
    wi = max(i for i, s in enumerate(starts) if s <= pos)
    shots.append({'id':shot_id,'chapter':chapter,'anchor':phrase,
                  'wordIndex':wi,'startMs':words[wi]['startMs']})
    search_from = pos+len(phrase)
shots[0]['startMs'] = 0
for i, shot in enumerate(shots):
    shot['endMs'] = shots[i+1]['startMs'] if i+1<len(shots) else timing['durationMs']
    shot['durationMs'] = shot['endMs']-shot['startMs']
    if shot['durationMs'] <= 0: raise RuntimeError(shot)
(ROOT/'src/shots-third.json').write_text(json.dumps(shots,indent=2),encoding='utf-8')
for shot in shots:
    print(f"{shot['startMs']/1000:6.2f}–{shot['endMs']/1000:6.2f} {shot['id']} ({shot['durationMs']/1000:.2f}s)")
