def is_tri(n):
    x = (-1 + (1+8*n)**0.5)/2
    if x - int(x) == 0:
        return True
    return False

def is_penta(n):
    x = (1 + (1+24*n)**0.5)/6
    if x - int(x) == 0:
        return True
    return False

def hexa(i):
    n = i*(2*i-1)
    return n

i = 2
while True:
    x = hexa(i)
    if is_tri(x) and is_penta(x):
        print(x)
    i+=1