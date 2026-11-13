# ai_overfitting.py - OMQ Python AI Overfitting
print('Overfitting: Zu viel gelernt!')
print('Schueler A: Lernt Muster! Train 95% / Test 93% = GUT!')
print('Schueler B: Lernt auswendig! Train 100% / Test 50% = OVERFITTING!')
train_a, test_a = 95, 93
train_b, test_b = 100, 50
print(f'A: Unterschied Train-Test = {train_a-test_a}% - Klein! Gut!')
print(f'B: Unterschied Train-Test = {train_b-test_b}% - RIESIG! Overfitting!')
print('Regel: Wenn Unterschied gross = Zu viel gemerkt!')
print('Fix: Mehr Daten! Einfacheres Modell!')
