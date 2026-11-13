# OMQ - EAL309 - R.419 - Nr.173 PYTHON 9 - FEHLER - TRY / EXCEPT!

## OMQ ist Fehler! OMQ ist EAL309! User tippt Blödsinn! Programm stürzt ab! Schrecklich! Rot! Panik! Try / Except = Airbag! Versuch es! Wenn Fehler, fang ihn! Sag nett: Hey, das war falsch! Programm lebt weiter! Kein Absturz! Profis machen IMMER Try / Except!

**Kai Olaf Ketelhut - Berlin - BLAK FAT12 - sol pattern omq**


### Try / Except!

| Code | Was? |
| --- | --- |
| try: | Versuch es! |
| except: | Wenn Fehler, mach das! |
| int('abc') | Fehler! Kann nicht Zahl sein! |

### Fehler-Regel!

**try = Versuch! except = Fang den Fehler! Programm stürzt NIE ab!**


```python
# fehler.py - OMQ Python Try / Except!
print('Teilen wir!')
try:
    a = int(input('Zahl 1? '))
    b = int(input('Zahl 2? '))
    print(f'{a} / {b} = {a / b}')
except ValueError:
    print('Hey! Das war keine Zahl! Versuch nochmal!')
except ZeroDivisionError:
    print('Hey! Durch 0 geht nicht!')
print('Programm lebt noch! Kein Absturz!')
```

CATIA V4/V5/V6/3DEXPERIENCE by Priplo - EAL309 R.419 - Nr.173

