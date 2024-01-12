from math import factorial as fct
count = 0
for n in range(1,101):
    for r in range(1,n):
        if (fct(n)/(fct(r)*fct(n-r))) > 1000000:
            print(n,r,fct(n)/(fct(r)*fct(n-r)))
            count += 1

print(count)