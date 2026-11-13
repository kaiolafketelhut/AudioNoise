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
