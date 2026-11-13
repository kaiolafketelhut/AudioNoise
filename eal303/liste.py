freunde = ['Kai', 'Lena', 'Max']
print('Meine Freunde:', freunde)
print('Erster Freund:', freunde[0])
print('Wie viele?', len(freunde))
freunde.append('Sara')
print('Jetzt:', freunde)
print('Jetzt sind es', len(freunde), 'Freunde!')
for f in freunde:
    print(f'Hallo {f}! Du bist cool!')
