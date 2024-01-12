def checkPal(i):
    i=str(i); l=len(i)
    if (l%2 and i[:l//2]==i[(l//2)+1:][::-1]) or (not(l%2) and i[:l//2]==i[(l//2):][::-1]):
        return True
    else:
        return False
    
total=0

for i in range(1000000):
    if checkPal(i) and checkPal(bin(i)[2:]):
        print(i,bin(i)[2:])
        total+=i

print(total)