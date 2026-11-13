# OMQ - EAL308 - R.418 - Nr.172 PYTHON 8 - DATEI - SPEICHERN!

## OMQ ist Datei! OMQ ist EAL308! Programm zu = Alles weg! Schrecklich! Datei = Merken für immer! Wie Notizbuch! Aufschreiben = Speichern! Lesen = Erinnern! So speichert jede App deine Daten! Ohne Datei = Goldfisch-Gedächtnis! Mit Datei = Elefant-Gedächtnis!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Datei!

| Code | Was? |
| --- | --- |
| open('x.txt','w') | Schreiben! w = write! |
| open('x.txt','r') | Lesen! r = read! |
| open('x.txt','a') | Anhängen! a = append! |
| with open(...) as f: | Auto-zu! Sicher! |

### Datei-Regel!

**w = Neu schreiben! r = Lesen! a = Hinten dran! Immer with benutzen!**


```python
# datei.py - OMQ Python Datei!
# Schreiben!
with open('tagebuch.txt', 'w') as f:
    f.write('Heute war cool!\n')
    f.write('Ich lerne Python!\n')
print('Gespeichert!')
# Anhängen!
with open('tagebuch.txt', 'a') as f:
    f.write('Noch ein Satz!\n')
# Lesen!
with open('tagebuch.txt', 'r') as f:
    inhalt = f.read()
    print('Tagebuch sagt:')
    print(inhalt)
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL308 R.418 - Nr.172

