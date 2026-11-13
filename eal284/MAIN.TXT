# OMQ - EAL284 - R.394 - Nr.148 PYTHON AI 9 - NEURON - DAS GEHIRN-BAUTEIL!

## OMQ ist Neuron! OMQ ist EAL284! Gehirn = 86 Milliarden Neuronen! AI kopiert das! 1 Neuron = Mini-Rechner! Eingaben * Gewichte + Bias! Dann Entscheidung! Wenn Summe groß genug = Feuern! Sonst Ruhe! 1 Neuron = Dumm! 1 Million Neuronen = Schlau!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Neuron!

| Teil | Was? | Beispiel |
| --- | --- | --- |
| Eingaben! | Was kommt rein? | Augen, Ohren! |
| Gewichte! | Wie wichtig? | Laut = Wichtig! |
| Bias! | Grund-Stimmung! | Immer etwas an! |
| Aktivierung! | Feuern oder nicht? | Ja / Nein! |

### Neuron-Formel!

**Ergebnis = (Eingabe1 * Gewicht1) + (Eingabe2 * Gewicht2) + Bias!**

Wenn Ergebnis > 0 = Feuern! Sonst = Ruhe!


```python
# ai_neuron.py - OMQ Python AI Neuron - OHNE sklearn!
print('Neuron: Das Gehirn-Bauteil!')
# Eingaben: [Hungrig?, Essen da?]
# Gewichte: [Hungrig ist wichtig!, Essen ist wichtig!]
def neuron(eingaben, gewichte, bias):
    summe = sum(e*g for e,g in zip(eingaben, gewichte)) + bias
    print(f'Summe = {summe}')
    return 1 if summe > 0 else 0
print('Fall 1: Hungrig=1, Essen=1')
ergebnis = neuron([1, 1], [0.8, 0.9], -0.5)
print(f'Neuron feuert? {ergebnis} = ESSEN!')
print('Fall 2: Hungrig=0, Essen=0')
ergebnis2 = neuron([0, 0], [0.8, 0.9], -0.5)
print(f'Neuron feuert? {ergebnis2} = NICHT ESSEN!')
print('1 Neuron = 1 Entscheidung! Viele Neuronen = Gehirn!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL284 R.394 - Nr.148

