# ai_chatbot.py - OMQ Python AI Chatbot - DEIN EIGENER BOT!
print('OMQ Chatbot: Hallo! Ich bin OMQ-Bot! Frag mich was! (tippe ende zum Beenden)')
antworten = {
    'hallo': 'Hallo! Schoen dich zu sehen! Wie geht es dir?',
    'wie geht': 'Mir geht es super! Ich bin Code! Und dir?',
    'katze': 'Katzen sind die besten! Sie schnurren, wenn sie gluecklich sind!',
    'berlin': 'Berlin ist die Hauptstadt von Deutschland! Und Heimat von OMQ!',
    'wer bist du': 'Ich bin OMQ-Bot! Gebaut von Kai! EAL290! R.400!',
    'danke': 'Gerne! Immer wieder! OMQ hilft!',
}
while True:
    frage = input('Du: ').lower()
    if frage == 'ende':
        print('Bot: Tschuess! Bis bald! OMQ!')
        break
    gefunden = False
    for wort, antwort in antworten.items():
        if wort in frage:
            print(f'Bot: {antwort}')
            gefunden = True
            break
    if not gefunden:
        print('Bot: Hmm, das verstehe ich noch nicht! Aber ich lerne! Frag mich nach Katze, Berlin oder Hallo!')
