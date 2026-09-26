"""Sentence-aware, quiet phrase captions from actual Andrew word times."""
def build_captions(words):
    result = []
    names = {('little', 'universe'), ('x', 'doctor'), ('show', 'notes'), ('27', 'minutes'), ('hundred','hours')}
    def push(items):
        if items:
            text = ' '.join(w['text'] for w in items).replace('came up my hometown.', 'came up — my hometown.')
            result.append({'text': text,
                           'startMs': items[0]['startMs'], 'endMs': items[-1]['endMs'],
                           'timestampMs': None, 'confidence': None})
    sentences, sentence = [], []
    for word in words:
        sentence.append(word)
        if word['text'].endswith(('.', '?', '!')):
            sentences.append(sentence);sentence=[]
    if sentence:sentences.append(sentence)
    for sentence in sentences:
        while sentence:
            if len(sentence)<=12 and len(' '.join(w['text'] for w in sentence))<=86 and sentence[-1]['endMs']-sentence[0]['startMs']<=4300:
                push(sentence);break
            candidates=[]
            for i in range(3,len(sentence)-2):
                left,right=sentence[:i],sentence[i:]
                pair=(left[-1]['text'].lower().strip('.,:!?'),right[0]['text'].lower().strip('.,:!?'))
                if pair in names or len(' '.join(w['text'] for w in left))>86:continue
                time=left[-1]['endMs']-left[0]['startMs']
                if time>3800:continue
                boundary=left[-1]['text'].endswith((',',':',';')) or right[0]['text'].lower() in ['and','but','with','while','then','instead']
                score=abs(i-min(8,len(sentence)/2))-(3 if boundary else 0)
                candidates.append((score,i))
            if not candidates:
                push(sentence);break
            _,i=min(candidates)
            push(sentence[:i]);sentence=sentence[i:]
    return result
