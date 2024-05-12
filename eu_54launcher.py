import eu_54v2 as play

wins1, wins2 = 0,0

with open('0054_poker.txt') as f1:
    for line in f1.readlines():
        h1, h2 = line[:14], line[15:]
        w = play.poker(h1,h2)
        if w == 'hand1':
            print('one')
            wins1 += 1
        elif w == 'hand2':
            print('two')
            wins2 += 1
        else:
            pass

print(f'wins1:{wins1}  wins2:{wins2}')