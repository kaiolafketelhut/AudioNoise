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
