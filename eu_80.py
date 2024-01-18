import decimal,math
decimal.getcontext().prec=105

t_sum=0
for i in range(2,101):
    if i not in {4,9,16,25,36,49,64,81,100}:
        num=decimal.Decimal(i).sqrt()
        # print(num)
        t_sum+=sum([int(j) for j in str(num)[2:101]])+math.floor(num)

print(t_sum)