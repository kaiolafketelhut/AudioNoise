import random, os
max_zahl = int(os.getenv('INPUT_MAX-ZAHL', '100'))
geheim = random.randint(1, max_zahl)
print(f'OMQ Rate-Spiel! Ich denke an 1-{max_zahl}!')
low, high, versuche = 1, max_zahl, 0
while low <= high:
    tipp = (low + high) // 2
    versuche += 1
    print(f'Versuch {versuche}: Ich tippe {tipp}...')
    if tipp < geheim:
        print('Zu klein! Hoeher!')
        low = tipp + 1
    elif tipp > geheim:
        print('Zu gross! Tiefer!')
        high = tipp - 1
    else:
        print(f'GEWONNEN! Geheim war {geheim}! In {versuche} Versuchen!')
        break
