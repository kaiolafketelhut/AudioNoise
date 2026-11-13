# OMQ - EAL285 - R.395 - Nr.149 PYTHON AI 10 - NEURAL NETWORK - VIELE NEURONEN!

## OMQ ist Neural Network! OMQ ist EAL285! 1 Neuron = Dumm! Viele Neuronen in Schichten = Schlau! Input-Schicht = Augen! Hidden-Schicht = Denken! Output-Schicht = Antwort! Wie Fabrik! Jede Schicht macht einen Schritt! Zusammen = Verstehen!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Neural Network!

| Schicht | Was? | Beispiel |
| --- | --- | --- |
| Input! | Eingaben! | Bild kommt rein! |
| Hidden! | Denken! | Kanten? Formen? |
| Output! | Antwort! | Katze! Hund! |

### Network-Regel!

1. **Input -> Hidden!** Jeder Hidden-Neuron rechnet!

2. **Hidden -> Output!** Weitergeben!

3. **Lernen = Gewichte ändern!** Falsche Antwort = Gewichte fixen!


```python
# ai_network.py - OMQ Python AI Neural Network - OHNE sklearn!
print('Neural Network: Viele Neuronen!')
def neuron(eingaben, gewichte, bias):
    summe = sum(e*g for e,g in zip(eingaben, gewichte)) + bias
    return 1 if summe > 0 else 0
# Input: [Hat Fell?, Bellt?]
inputs = [1, 1]
print(f'Input: Fell=1, Bellt=1')
# Hidden-Schicht: 2 Neuronen!
h1 = neuron(inputs, [0.5, 0.5], -0.2)
h2 = neuron(inputs, [0.9, -0.5], -0.2)
print(f'Hidden: h1={h1} (Tier?), h2={h2} (Hund-artig?)')
# Output-Schicht: 1 Neuron!
output = neuron([h1, h2], [0.5, 0.8], -0.5)
print(f'Output: {output}')
print('Antwort: 1 = HUND! 0 = KATZE!')
print('Netzwerk: Input -> Hidden -> Output! So denkt AI!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL285 R.395 - Nr.149

