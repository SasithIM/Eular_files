max_sum = 0
for i in range(1,100):
    for j in range(1,100):
        snum = sum([int(k) for k in str(i**j)])
        max_sum = snum if snum>max_sum else max_sum

print(max_sum)