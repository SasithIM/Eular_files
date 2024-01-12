for j in range(1,7):
    total = 0
    for i in range(10**j):
        if(not(i % 3) or not(i % 5)):
            total += i
    print(total)
