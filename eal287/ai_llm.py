# ai_llm.py - OMQ Python AI LLM - Mini ChatGPT
print('LLM: Naechstes Wort raten!')
wissen = {
    'Die Katze sitzt auf dem': 'Dach',
    'Ich trinke gerne': 'Kaffee',
    'Berlin ist die Hauptstadt von': 'Deutschland',
    'Der Himmel ist': 'blau',
}
def llm_antwort(frage):
    print(f'Prompt: {frage}')
    antwort = wissen.get(frage, '...weiss ich nicht...')
    print(f'LLM raet naechstes Wort: {antwort}')
    return antwort
llm_antwort('Die Katze sitzt auf dem')
llm_antwort('Ich trinke gerne')
llm_antwort('Berlin ist die Hauptstadt von')
print('Echtes LLM = Dasselbe, nur mit Milliarden Woertern!')
print('Raten! Raten! Raten! = Text!')
