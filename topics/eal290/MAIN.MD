# OMQ - EAL290 - R.400 - Nr.154 PYTHON AI 15 - AI PROJEKT - DEIN EIGENER CHATBOT!

## OMQ ist Chatbot! OMQ ist EAL290! R.400! JUBILÄUM! Du hast gelernt: Neuron! Network! Deep Learning! LLM! Prompt! Ethik! Jetzt: Alles zusammen! Dein eigener Chatbot! Kein ChatGPT! Kein Internet! Nur Python! Du fragst! Er antwortet! Wie ein echter Bot! 154 Konzepte! Du bist AI-Profi!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Chatbot!

| Teil | Was? | EAL |
| --- | --- | --- |
| Neuron! | 1 Entscheidung! | EAL284! |
| Network! | Viele Neuronen! | EAL285! |
| LLM! | Nächstes Wort! | EAL287! |
| Prompt! | Richtig fragen! | EAL288! |

### Chatbot-Regel!

1. **Eingabe lesen!** Was will User?

2. **Muster finden!** Hallo? Frage? Abschied?

3. **Antwort wählen!** Beste Antwort geben!

4. **Fair bleiben!** Ethik! EAL289!


```python
# ai_chatbot.py - OMQ Python AI Chatbot - DEIN EIGENER BOT!
print('OMQ Chatbot: Hallo! Ich bin OMQ-Bot! Frag mich was! (tippe ende zum Beenden)')
antworten = {
    'hallo': 'Hallo! Schön dich zu sehen! Wie geht es dir?',
    'wie geht': 'Mir geht es super! Ich bin Code! Und dir?',
    'katze': 'Katzen sind die besten! Sie schnurren, wenn sie glücklich sind!',
    'berlin': 'Berlin ist die Hauptstadt von Deutschland! Und Heimat von OMQ!',
    'wer bist du': 'Ich bin OMQ-Bot! Gebaut von Kai! EAL290! R.400!',
    'danke': 'Gerne! Immer wieder! OMQ hilft!',
}
while True:
    frage = input('Du: ').lower()
    if frage == 'ende':
        print('Bot: Tschüss! Bis bald! OMQ!')
        break
    gefunden = False
    for wort, antwort in antworten.items():
        if wort in frage:
            print(f'Bot: {antwort}')
            gefunden = True
            break
    if not gefunden:
        print('Bot: Hmm, das verstehe ich noch nicht! Aber ich lerne! Frag mich nach Katze, Berlin oder Hallo!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL290 R.400 - Nr.154

