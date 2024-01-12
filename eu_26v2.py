import decimal as d
d.getcontext().prec = 100

num_list = {}

def trim(num):
    num =str(num)[2:]
    for i in range(3):
        if(num[0] == '0'):
            num = num[1:]
    return num
    

for i in range(11,999):
    n = d.Decimal(1)/d.Decimal(i)
    num_list[i] = trim(n)

r = 7

while len(num_list)>2:
    delkeys = {}
    for i in num_list:
        flag = True
        x = num_list[i]
        j=0
        for k in range(1,6):
            if x[:k]==x[k:2*k]:
                delkeys[i]=i
                flag = False
                break
        while flag:
            if (x[j:j+r]==x[j+r:j+2*r]):
                delkeys[i]=i
                break
            j+=1
            if j>4:
                break
    for k in delkeys:
        del num_list[k]
    r+=1

print(num_list)

# deosn't work