from decimal import Decimal, getcontext
def is_prime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True
def decimal_p(p):
    getcontext().prec = 10000
    x = Decimal((10*(p-1) - 1 ))/Decimal(p)
    return x
def rec_count(n):
    n=str(n)[2:]
    i=2 ; j=3
    while n[:i]!=n[i:j]:
        i+=1
        j = i*2
        if j>10000:
            return 0
    return len(n[i:j])

max_length=0 ; max_num=1
for i in range(1,1000):
    if is_prime(i):
        if rec_count(decimal_p(i))>max_length:
            max_length=rec_count(decimal_p(i))
            max_num = i 
print(max_num,max_length)




