import math
num1 = math.factorial(100)
num1 = str(num1)
total = 0
for i in num1:
    total += int(i)
print(total)