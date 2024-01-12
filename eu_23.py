import divisors as div

ab_nums = []
sums =  {}

for i in range(1,28123):
    d = div.divisors(i)
    d = sum(d[:-1])
    if i < d:
        ab_nums.append(i)

for i in range(len(ab_nums)):
    for j in ab_nums[i:]:
        new_sum = ab_nums[i] + j
        if new_sum < 28123:
            if new_sum not in sums:
                sums[new_sum] = f'{ab_nums[i]} + {j}'
        else:
            break
sums = sorted(sums)[::-1]

for i in range(len(sums)):
    if sums[i]-sums[i+1]==1:
        continue
    else:
        print(sum([j for j in range(sums[i])])-sum(sums[i+1:]))
        break