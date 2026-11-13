# ai_sklearn.py - OMQ - OHNE sklearn - Reines Python!
print('Scikit-Learn Ersatz: Echte AI - Ohne Install!')
# X = Stunden, y = Punkte - Wir lernen die Formel selbst!
X = [1,2,3,4,5]
y = [10,20,30,40,50]
# Mittelwert
mx = sum(X)/len(X)
my = sum(y)/len(y)
# Steigung = Wie viel Punkte pro Stunde?
steigung = sum((x-mx)*(yy-my) for x,yy in zip(X,y)) / sum((x-mx)**2 for x in X)
print(f'AI trainiert! Hat gelernt: 1 Stunde = {steigung:.0f} Punkte!')
vor = steigung * 6
print(f'Vorhersage: 6 Stunden lernen = {vor:.0f} Punkte!')
print('Echte AI! Ohne sklearn! Läuft!')
