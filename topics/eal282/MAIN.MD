# OMQ - EAL282 - R.392 - Nr.146 PYTHON AI 7 - KLASSIFIKATION - OHNE SKLEARN!

## OMQ ist Klassifikation! OMQ ist EAL282! Regression = Zahl raten! Klassifikation = Kategorie raten! Katze oder Hund? Ja oder Nein? Spam oder Kein Spam? Kein sklearn nötig! Wir machen es selbst! Einfach! Abstand messen! Nächster Nachbar gewinnt!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Klassifikation!

| | Regression | Klassifikation |
| --- | --- | --- |
| Rät | Zahl! 60 Punkte! | Kategorie! Katze! |
| Beispiel | Wie viele Punkte? | Katze oder Hund? |

### Regel: Nächster Nachbar!

1. **Merke alle Beispiele!**

2. **Neues Tier kommt! Miss Abstand zu allen!**

3. **Nächster Nachbar = Antwort!**


```python
# ai_klassifikation.py - OMQ Python AI OHNE sklearn - Läuft ÜBERALL!
print('Klassifikation: Katze oder Hund? Ohne sklearn!')
# [Gewicht kg, Ohren: 0=rund, 1=spitz] -> Tier
training = [([2, 1], 'Katze'), ([3, 1], 'Katze'), ([20, 0], 'Hund'), ([25, 0], 'Hund')]
neu = [4, 1]
print(f'Neues Tier: {neu} - Gewicht 4kg, Spitz-Ohren!')
# Abstand zu allen!
for beispiel, tier in training:
    abstand = abs(beispiel[0]-neu[0]) + abs(beispiel[1]-neu[1])
    print(f'Abstand zu {tier} {beispiel}: {abstand}')
print('Nächster: Katze! Antwort: KATZE!')
print('Klassifikation ohne sklearn! Läuft in Termux!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL282 R.392 - Nr.146

