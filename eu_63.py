count=0
for n in range(1,100):
    for i in range(1,10**n):
        if len(str(i**n))==n:
            count+=1
            print(i**n,n)
        elif len(str(i**n))>n:
            break
print(count)