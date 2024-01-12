total = 0;x=0
for i in range(1,1000):
    x = i**i
    total+=x
print(str(total)[-10::])
