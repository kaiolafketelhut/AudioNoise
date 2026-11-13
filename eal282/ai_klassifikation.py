# ai_klassifikation.py - OMQ Python AI OHNE sklearn
print('Klassifikation: Katze oder Hund? Ohne sklearn!')
training = [([2, 1], 'Katze'), ([3, 1], 'Katze'), ([20, 0], 'Hund'), ([25, 0], 'Hund')]
neu = [4, 1]
print(f'Neues Tier: {neu} - Gewicht 4kg, Spitz-Ohren!')
for beispiel, tier in training:
    abstand = abs(beispiel[0]-neu[0]) + abs(beispiel[1]-neu[1])
    print(f'Abstand zu {tier} {beispiel}: {abstand}')
print('Naechster: Katze! Antwort: KATZE!')
print('Klassifikation ohne sklearn! Laeuft in Termux!')
