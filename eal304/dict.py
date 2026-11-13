kai = {'name': 'Kai', 'alter': 18, 'stadt': 'Berlin', 'cool': True}
print(kai)
print('Name:', kai['name'])
print('Stadt:', kai['stadt'])
kai['lieblingsessen'] = 'Döner'
print('Jetzt:', kai)
print('Alle Schlüssel:', list(kai.keys()))
for k, v in kai.items():
    print(f'{k} = {v}')
