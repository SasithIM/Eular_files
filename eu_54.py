hand1 ='8C TS KC 9H 4S'; hand2 = '7D 2S 5D 3S AC'

class Card:
    def __init__(self,val,suit) -> None:
        self.suit = suit
        if val=='A':
            self.val = 14
        elif val=='K':
            self.val=13
        elif val=='Q':
            self.val=12
        elif val=='J':
            self.val=11
        elif val=='T':
            self.val=10
        else:
            self.val = int(val)
        

def hands(cardstr):
    cards=[]
    for i in cardstr.split(' '):
        cards.append(i)
    return cards

def Game(hand1,hand2):
    val1,val2,sut1,sut2 = [],[],[],[]
    for i in range(5):
        val1.append(hand1[i].val)
        val2.append(hand2[i].val)
        sut1.append(hand1)

