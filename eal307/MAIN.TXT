# OMQ - EAL307 - R.417 - Nr.171 PYTHON 7 - IF / ELSE - ENTSCHEIDEN!

## OMQ ist Entscheiden! OMQ ist EAL307! Computer ohne If = Dumm! Macht IMMER das Gleiche! Mit If = Computer DENKT! Wenn Wetter gut, dann raus! Sonst drinnen! Wenn Passwort richtig, dann rein! Sonst raus! If = Gabelung! Wie im Leben: Wenn... dann... sonst...

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### If / Else!

| Code | Was? |
| --- | --- |
| if alter >= 18: | Wenn Bedingung wahr! |
| elif ...: | Sonst wenn! |
| else: | Sonst! |

### If-Regel!

**if = Wenn! elif = Sonst wenn! else = Sonst! Einrückung ist Pflicht!**


```python
# entscheiden.py - OMQ Python If!
alter = int(input('Wie alt bist du? '))
if alter >= 18:
    print('Du darfst rein! Erwachsen!')
elif alter >= 12:
    print('Du darfst mit Mama rein!')
else:
    print('Noch zu jung! Sorry!')
passwort = input('Passwort? ')
if passwort == 'omq123':
    print('Willkommen! Passwort richtig!')
else:
    print('Falsch! Raus!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL307 R.417 - Nr.171

