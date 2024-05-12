def count(num):
    counter = 0
    if num==2:
        counter+=2
    else:
        counter+=count(num-1)
    return counter

def count2(num):
    counter2=0
    for i in range(num,num//2,-1):
        counter2+=count(num)
    return counter2

print(count2(6))