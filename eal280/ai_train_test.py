# ai_train_test.py - OMQ - Train/Test OHNE sklearn!
print('Train/Test: Nicht schummeln! Ohne sklearn!')
X = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
# 80% Train, 20% Test - Einfach teilen!
X_train, y_train = X[:8], y[:8]
X_test, y_test = X[8:], y[8:]
print(f'Train: {len(X_train)} Fragen zum Lernen!')
print(f'Test: {len(X_test)} Neue Fragen zur Prüfung!')
mx = sum(X_train)/len(X_train)
my = sum(y_train)/len(y_train)
steigung = sum((x-mx)*(yy-my) for x,yy in zip(X_train,y_train)) / sum((x-mx)**2 for x in X_train)
fehler = sum(abs(steigung*x - yy) for x,yy in zip(X_test,y_test))
print(f'Ehrliche Prüfung: Fehler = {fehler:.0f} - Fast perfekt!')
print('Nicht geschummelt! Echte AI! Ohne sklearn!')
