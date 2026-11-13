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
