card_num = ['one', 'two', 'three', 'four', 'five']

# a class to contain each value and suite for each card
class Card:
    val = 0
    suit = ''
    def __init__(self,str1) -> None:
        self.suit = str1[1]
        try:
            self.val = int(str1[0])
        except:
            match str1[0]:
                case 'T':
                    t = 10
                case 'J':
                    t = 11
                case 'Q':
                    t = 12
                case 'K':
                    t = 13
                case 'A':
                    t = 14
            self.val = t
    
# a class to contain a hand of five cards
class Hand:
    one, two, three, four, five = [Card for i in range(5)]
    sortd = []
    def __init__(self,str2) -> None:
        temp = str2.split(' ')
        for num,card in zip(card_num,temp):
            setattr(self,num,Card(card))
        setattr(self,'sortd',sorted([card.val for card in [self.one, self.two, self.three, self.four, self.five]]))


def rs_flush(hand1:Hand) -> int:
    '''royal or straight flush'''
    if flush(hand1):
        temp = straight(hand1)
        if temp == 10:
            print('royal_flush')
            return 2 # royal flush
        elif temp != 0:
            print('straight_flush')
            return 1 # straight flush
        else:
            return 0 # no consecetive cards
    else:
        return 0 

def straight(hand1:Hand) -> int:
    '''straight'''
    temp = hand1.sortd.copy()
    for i in range(4,0,-1):
        temp[i] = temp[i]-temp[i-1]
    if temp[1:] == [1,1,1,1]:
        return temp[0]
    else:
        return 0

def flush(hand1:Hand) -> int:
    '''flush'''
    return all(card.suit == hand1.one.suit for card in [hand1.one,hand1.two, hand1.three, hand1.four, hand1.five])


def four_of_kind(hand1:Hand)-> int:
    '''four cards of the same value'''
    return n_of_kind(hand1,4)[-1]

def three_of_kind(hand1:Hand) -> int:
    '''three cards of the same value'''
    return n_of_kind(hand1,3)[-1]

def pairs(hand1:Hand) -> int:
    '''pairs of same values'''
    temp = n_of_kind(hand1,2)
    if n_of_kind(hand1,3) != temp:
        if len(temp)>2:
            return 14+temp[-1]
        else:
            return temp[-1]
    else:
        return 0
    
def full_house(hand1:Hand) -> int:
    '''pair and three of a kind'''
    return pairs(hand1) and n_of_kind(hand1,3)[-1]

def n_of_kind(hand1:Hand, n:int) -> list:
    '''n = number of equal values'''
    temp = hand1.sortd
    temp2 = {0:0}
    for i in range(5-n+1):
        if temp[i] == temp[i+n-1]:
            if temp[i] in temp2:
                temp2[temp[i]] += 1
            else:
                temp2[temp[i]] = 1
        else:
            pass
    # print(sorted(list(temp2.keys())))
    return sorted(list(temp2.keys()))

def high_card(hand1:Hand,hand2:Hand) -> str:
    '''highest card'''
    for c1,c2 in zip(hand1.sortd[::-1],hand2.sortd[::-1]):
        if c1==c2:
            pass
        elif c1>c2:
            return 'hand1'
        elif c2>c1:
            return 'hand2'
    else:
        return 'draw'

# the game.
def poker(h1:str, h2:str) -> str:
    '''play poker'''
    hand1 = Hand(h1)
    hand2 = Hand(h2)
    checks = [rs_flush,four_of_kind,full_house,flush,straight,three_of_kind,pairs]

    for check in checks:
        r1 = check(hand1)
        r2 = check(hand2)

        if r1==r2:
            pass
        elif r1>r2:
            # print(check)
            return 'hand1'
        elif r2>r1:
            # print(check)
            return 'hand2'
    else:
        return high_card(hand1,hand2)
        

# h1,h2 = 'AS KD 3D JD 8H','7C 8C 5C QD 6C'
# print(poker(h1,h2))
# print(h1.sortd)