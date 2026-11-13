# ai_deep.py - OMQ Python AI Deep Learning
print('Deep Learning: Viele Schichten!')
def schicht(name, eingabe, was):
    print(f'{name}: {eingabe} -> Versteht: {was}')
    return was
print('Bild kommt rein: Pixel!')
s1 = schicht('Schicht 1', 'Pixel', 'Kanten!')
s2 = schicht('Schicht 2', s1, 'Formen: Ohren, Nase!')
s3 = schicht('Schicht 3', s2, 'Gesichtsteile: Augen, Mund!')
s4 = schicht('Schicht 4', s3, 'GESICHT! Das ist eine KATZE!')
print('Deep = Jede Schicht versteht mehr!')
print('Flach = 1 Schicht! Deep = Viele Schichten!')
