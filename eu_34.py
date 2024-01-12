from math import factorial as fct

def isDigitfr(num):
    '''check if a number given is a digit factorial and return a bool'''
    if num==sum([fct(int(i)) for i in str(num)]):
        return True
    else:
        return False
    
def checkDigitFr(i,n=0):
    if not(((i-n)//5)%2):
        if isDigitfr(i):
            num_ls.append(i)

    
num_ls = []
                                # basic verison...
for i in range(3,999000):
    if isDigitfr(i):
        num_ls.append(i)


# here to...

# for i in range(3,45):
#     checkDigitFr(i)

# for i in range(100,999):
#     checkDigitFr(i,2)

# for i in range(1000,9999):
#     checkDigitFr(i,3)

# for i in range(10000,99999):
#     checkDigitFr(i,4)

# for i in range(100000,999000):
#     checkDigitFr(i,5)

                            # ...here is a different version

# for i in range(1,4):
#     for j in range(1,4):
#         k=10*i+j
#         if k==isDigitfr(k):
#             num_ls.append(k)

print(sum(num_ls))


#  factoarials for each digit:
# 0: 1, 
# 1: 1, 
# 2: 2, 
# 3: 6, 
# 4: 24,      limit for2 digit
# 5: 120, 
# 6: 720,         limit for 3 digit
# 7: 5040,          4
# 8: 40320,         5
# 9: 362880         6 and up