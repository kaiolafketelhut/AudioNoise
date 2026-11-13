def sag_hallo(name):
    return f'Hallo {name}! Du bist cool!'

def plus(a, b):
    return a + b

def ist_erwachsen(alter):
    return alter >= 18

print(sag_hallo('Kai'))
print(sag_hallo('Lena'))
print('3 + 5 =', plus(3, 5))
print('Kai erwachsen?', ist_erwachsen(18))
print('Max erwachsen?', ist_erwachsen(12))
