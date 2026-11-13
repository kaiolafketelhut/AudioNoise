# ai_network.py - OMQ Python AI Neural Network
print('Neural Network: Viele Neuronen!')
def neuron(eingaben, gewichte, bias):
    summe = sum(e*g for e,g in zip(eingaben, gewichte)) + bias
    return 1 if summe > 0 else 0
inputs = [1, 1]
print(f'Input: Fell=1, Bellt=1')
h1 = neuron(inputs, [0.5, 0.5], -0.2)
h2 = neuron(inputs, [0.9, -0.5], -0.2)
print(f'Hidden: h1={h1} (Tier?), h2={h2} (Hund-artig?)')
output = neuron([h1, h2], [0.5, 0.8], -0.5)
print(f'Output: {output}')
print('Antwort: 1 = HUND! 0 = KATZE!')
print('Netzwerk: Input -> Hidden -> Output! So denkt AI!')
