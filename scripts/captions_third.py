"""Keep spoken product and creator names together in caption groups."""
import json
from pathlib import Path

def build_captions(words):
    captions, group = [], []
    names = {('little', 'universe'), ('x', 'doctor'), ('show', 'notes')}
    def push(items):
        if items:
            captions.append({'text': ' '.join(w['text'] for w in items),
                             'startMs': items[0]['startMs'], 'endMs': items[-1]['endMs']})
    for word in words:
        if group and (word['endMs'] - group[0]['startMs'] > 2200 or len(group) >= 7):
            pair = (group[-1]['text'].lower().strip('.,:!?'), word['text'].lower().strip('.,:!?'))
            carry = [group.pop()] if pair in names else []
            push(group)
            group = carry
        group.append(word)
    push(group)
    return captions

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    words = json.loads((root / 'src/words-third.json').read_text(encoding='utf-8'))
    captions = build_captions(words)
    (root / 'src/captions-third.json').write_text(json.dumps(captions, indent=2), encoding='utf-8')
    print('Caption groups:', len(captions))
