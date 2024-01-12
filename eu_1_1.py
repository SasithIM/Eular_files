for j in range(1,7):
    arr=[]
    for i in range(10**j):
        if(i%3==0 or i%5==0):
            arr.append(i)
    print(sum(arr))
