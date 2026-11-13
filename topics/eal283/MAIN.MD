# OMQ - EAL283 - R.393 - Nr.147 PYTHON AI 8 - OVERFITTING - ZU VIEL GELERNT!

## OMQ ist Overfitting! OMQ ist EAL283! AI lernt zu viel! Merkt sich alle Antworten auswendig! Wie Schüler der nur alte Prüfungen lernt! Neue Prüfung = Durchgefallen! Merken ist NICHT Verstehen! Gute AI = Versteht Muster! Schlechte AI = Merkt sich alles!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Overfitting!

| | Gut! Verstehen! | Schlecht! Auswendig! |
| --- | --- | --- |
| Train-Note | 95%! | 100%! |
| Test-Note | 93%! | 50%! |
| Merken | Muster! | Alle Antworten! |

### Anti-Overfitting!

1. **Mehr Daten!** Nicht 10, sondern 1000!

2. **Einfaches Modell!** Nicht kompliziert!

3. **Train/Test prüfen!** Wenn Train 100% aber Test 50% = Overfitting!


```python
# ai_overfitting.py - OMQ Python AI Overfitting - OHNE sklearn!
print('Overfitting: Zu viel gelernt!')
print('Schüler A: Lernt Muster! Train 95% / Test 93% = GUT!')
print('Schüler B: Lernt auswendig! Train 100% / Test 50% = OVERFITTING!')
train_a, test_a = 95, 93
train_b, test_b = 100, 50
print(f'A: Unterschied Train-Test = {train_a-test_a}% - Klein! Gut!')
print(f'B: Unterschied Train-Test = {train_b-test_b}% - RIESIG! Overfitting!')
print('Regel: Wenn Unterschied groß = Zu viel gemerkt!')
print('Fix: Mehr Daten! Einfacheres Modell!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL283 R.393 - Nr.147

