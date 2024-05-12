from math import ceil
from decimal import *

getcontext().prec = (10000)

# k =int(input())
a = Decimal(2)


def nk(k):
    return (((1+a.sqrt())**(4*k)-2+(1-a.sqrt())**(4*k))/32).to_integral_value(rounding=ROUND_CEILING)

for i in range(100):
    print(nk(i)%20)