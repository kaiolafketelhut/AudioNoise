import random

def spielen():
    geheim = random.randint(1, 100)
    versuche = 0
    print('Ich denke an eine Zahl 1-100! Rate!')
    while True:
        try:
            tipp = int(input('Dein Tipp? '))
        except ValueError:
            print('Nur Zahlen bitte!')
            continue
        versuche += 1
        if tipp < geheim:
            print('Zu klein! Höher!')
        elif tipp > geheim:
            print('Zu groß! Tiefer!')
        else:
            print(f'GEWONNEN! In {versuche} Versuchen!')
            with open('best.txt', 'w') as f:
                f.write(f'Best: {versuche} Versuche!')
            break
spielen()
