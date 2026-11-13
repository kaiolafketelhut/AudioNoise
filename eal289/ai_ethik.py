# ai_ethik.py - OMQ Python AI Ethik
print('AI Ethik: Darf AI alles?')
bewerber = [('Anna', 90), ('Ben', 85), ('Cem', 95)]
print('Bewerber (Name, Punkte):', bewerber)
bester = max(bewerber, key=lambda x: x[1])
print(f'Faire AI waehlt: {bester[0]} - Weil beste Punkte! Fair!')
print('Unfaire AI wuerde sagen: Ben, weil Name klingt wie... - UNFAIR! VERBOTEN!')
print('Regel: AI darf nur auf LEISTUNG schauen! Nie auf Name, Haut, Geschlecht!')
print('Mensch prueft am Ende immer!')
