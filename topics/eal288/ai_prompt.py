# ai_prompt.py - OMQ Python AI Prompt Engineering
print('Prompt Engineering: Richtig fragen!')
def ai(prompt):
    if len(prompt) < 20:
        return 'Antwort: ...aeh... Katzen sind... Tiere? (Zu vage!)'
    else:
        return 'Antwort: Perfekt! Klarer Prompt = Klare Antwort! Katzen schnurren, weil sie gluecklich sind!'
print('Schlecht:')
print(ai('Schreib was ueber Katzen!'))
print('')
print('Gut:')
print(ai('Du bist Tierarzt! Erklaere in 3 Saetzen, warum Katzen schnurren, fuer Kinder!'))
print('Regel: Rolle + Aufgabe + Format + Beispiel = Perfekter Prompt!')
