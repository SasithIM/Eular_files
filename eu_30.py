total = 0
for num in range(2,999999):
    sums = [int(i)**5 for i in str(num)]
    if (num == sum(sums)):
        total += num
print(total)