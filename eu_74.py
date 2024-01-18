from math import factorial
def fact_sum(num):
    f_sum=0
    for i in str(num):
        f_sum+=factorial(int(i))
    return f_sum

def fact_chain(num):
    fc_set=set()
    while True:
        fc_set.add(num)
        num = fact_sum(num)
        if num in fc_set:
            break
    return len(fc_set)

count=0
for i in range(10**6):
    if fact_chain(i)==60:
        count+=1
print(count)