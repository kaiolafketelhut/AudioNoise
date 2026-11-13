# OMQ - EAL310 - R.420 - Nr.174 PYTHON 10 - PROJEKT - RATE-SPIEL!

## OMQ ist Projekt! OMQ ist EAL310! Du hast ALLES gelernt! Variable! Liste! Dictionary! Schleife! Funktion! If! Datei! Fehler! Jetzt BAUST du was Echtes! Rate-Spiel! Computer denkt sich Zahl! Du rätst! Zu hoch? Zu tief? Gewonnen! Das ist dein erstes ECHTES Spiel! Du bist jetzt Programmierer!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Rate-Spiel - Alles drin!

| Konzept | Wo? |
| --- | --- |
| Variable | geheim, versuche |
| Schleife | while True! |
| If / Else | Zu hoch / zu tief! |
| Try / Except | Falsche Eingabe! |
| Datei | Bestleistung speichern! |

### Projekt-Regel!

**Klein anfangen! Testen! Dann größer! Dein erstes Spiel = Dein Stolz!**


```python
# ratespiel.py - OMQ Python Projekt!
import random

def spielen():
    geheim = random.randint(1, 100)
    versuche = 0
    print('Ich denke an eine Zahl 1-100! Rate!')
    while True:
        try:
            tipp = int(input('Dein Tipp? '))
        except ValueError:
            print('Nur Zahlen bitte!')
            continue
        versuche += 1
        if tipp < geheim:
            print('Zu klein! Höher!')
        elif tipp > geheim:
            print('Zu groß! Tiefer!')
        else:
            print(f'GEWONNEN! In {versuche} Versuchen!')
            with open('best.txt', 'w') as f:
                f.write(f'Best: {versuche} Versuche!')
            break
spielen()
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL310 R.420 - Nr.174

