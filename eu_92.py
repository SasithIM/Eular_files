count=0

for i in range(1,10**7):
    num = i
    while True:
        temp=0
        for j in str(num):
            temp+=int(j)**2
        num=temp
        
        if num == 1:
            break
        elif num == 89:
            count+=1
            break
print(count)