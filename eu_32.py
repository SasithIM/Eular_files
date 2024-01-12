products = set()
s0 = [str(i) for i in range(1,10)]

for i in range(999):
    for j in range(100,9999):           #check if there is a way to lower the upper limit
        prd = i*j
        if prd>9999:
                continue
        else:
            s1 = sorted(f'{i}{j}{prd}')
            if s1 == s0:
                products.add(prd)
            else:
                pass
print(products)
print(sum(products))