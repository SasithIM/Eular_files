i=2
while True:
    if sorted(str(i)) == sorted(str(2*i)) == sorted(str(3*i)) == sorted(str(4*i)) == sorted(str(5*i)) ==sorted(str(6*i)):
        print(i)
        break
    else:
        i+=1