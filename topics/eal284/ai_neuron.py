# ai_neuron.py - OMQ Python AI Neuron
print('Neuron: Das Gehirn-Bauteil!')
def neuron(eingaben, gewichte, bias):
    summe = sum(e*g for e,g in zip(eingaben, gewichte)) + bias
    print(f'Summe = {summe}')
    return 1 if summe > 0 else 0
print('Fall 1: Hungrig=1, Essen=1')
ergebnis = neuron([1, 1], [0.8, 0.9], -0.5)
print(f'Neuron feuert? {ergebnis} = ESSEN!')
print('Fall 2: Hungrig=0, Essen=0')
ergebnis2 = neuron([0, 0], [0.8, 0.9], -0.5)
print(f'Neuron feuert? {ergebnis2} = NICHT ESSEN!')
print('1 Neuron = 1 Entscheidung! Viele Neuronen = Gehirn!')
