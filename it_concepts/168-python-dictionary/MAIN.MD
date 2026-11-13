# OMQ - EAL304 - R.414 - Nr.168 PYTHON 4 - DICTIONARY - SCHLUESSEL + WERT!

## OMQ ist Dictionary! OMQ ist EAL304! Liste = Nur Werte! Position 0,1,2! Aber was ist was? Dictionary = Schlüssel + Wert! Wie echtes Wörterbuch! Wort = Schlüssel! Erklärung = Wert! Wie Personalausweis! Name: Kai! Alter: 18! Stadt: Berlin! So speichert jede App deine Daten!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Dictionary!

| Code | Was? |
| --- | --- |
| kai = {'name': 'Kai'} | Dictionary machen! |
| kai['name'] | Wert holen mit Schlüssel! |
| kai['stadt'] = 'Berlin' | Neues Paar dazu! |
| kai.keys() | Alle Schlüssel! |

### Dictionary-Regel!

**Dictionary = { 'schlüssel': 'wert' }! Mit Schlüssel holen, nicht mit Zahl!**


```python
# dict.py - OMQ Python Dictionary!
kai = {'name': 'Kai', 'alter': 18, 'stadt': 'Berlin', 'cool': True}
print(kai)
print('Name:', kai['name'])
print('Stadt:', kai['stadt'])
kai['lieblingsessen'] = 'Döner'
print('Jetzt:', kai)
print('Alle Schlüssel:', list(kai.keys()))
for k, v in kai.items():
    print(f'{k} = {v}')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL304 R.414 - Nr.168

