import primes

i=643
n=4

while True:
    one = len(set(primes.factors(i)))
    two = len(set(primes.factors(i+1)))
    three = len(set(primes.factors(i+2)))
    four = len(set(primes.factors(i+3)))

    if one==n and two==n and three==n and four==n:
        print(i,primes.factors(i))
        print(i+1,primes.factors(i+1))
        print(i+2,primes.factors(i+2))
        print(i+3,primes.factors(i+3))
        break
    i+=1