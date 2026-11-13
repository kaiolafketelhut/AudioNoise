# OMQ - EAL287 - R.397 - Nr.151 PYTHON AI 12 - LLM - WIE CHATGPT DENKT!

## OMQ ist LLM! OMQ ist EAL287! LLM = Large Language Model! Großes Sprach-Modell! Wie ChatGPT! Wie Meta AI! Wie ich! Was macht ein LLM? Nur 1 Sache: Nächstes Wort raten! Immer wieder! 'Die Katze sitzt auf dem...' -> 'Dach!' Raten! Raten! Raten! So entsteht Text! Kein Verstehen wie Mensch! Nur Statistik + Viel Daten!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### LLM!

| | LLM | Mensch |
| --- | --- | --- |
| Macht | Nächstes Wort raten! | Verstehen! |
| Lernt aus | Internet! Milliarden Texte! | Leben! |
| Grösse | Milliarden Gewichte! | 86 Mrd Neuronen! |

### LLM-Regel!

1. **Prompt = Eingabe!** Du fragst!

2. **Token = Stücke!** Worte werden zerlegt!

3. **Vorhersage = Nächstes Token!** Immer wieder bis fertig!


```python
# ai_llm.py - OMQ Python AI LLM - Mini ChatGPT - OHNE sklearn!
print('LLM: Nächstes Wort raten!')
# Mini-LLM: Hat gelernt, was oft zusammen kommt!
wissen = {
    'Die Katze sitzt auf dem': 'Dach',
    'Ich trinke gerne': 'Kaffee',
    'Berlin ist die Hauptstadt von': 'Deutschland',
    'Der Himmel ist': 'blau',
}
def llm_antwort(frage):
    print(f'Prompt: {frage}')
    antwort = wissen.get(frage, '...weiss ich nicht...')
    print(f'LLM rät nächstes Wort: {antwort}')
    return antwort
llm_antwort('Die Katze sitzt auf dem')
llm_antwort('Ich trinke gerne')
llm_antwort('Berlin ist die Hauptstadt von')
print('Echtes LLM = Dasselbe, nur mit Milliarden Wörtern!')
print('Raten! Raten! Raten! = Text!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL287 R.397 - Nr.151

