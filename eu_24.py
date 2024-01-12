# see below.
import math
nums = [i for i in range(10)]
per = [];place = 0; i=9

while len(per)<10:
    while place<1000000:
        n = math.floor((1000000-place)/math.factorial(i))
        per.append(nums[n])
        place += math.factorial(i)*n
        nums.remove(nums[n])
        print(n,per,place,nums)
        i-=1

    if len(nums):
        nums.append(per[-1])
        x = per[-1]; y = nums[-2]
        nums.sort()
        per = per[:-1]
        per.append(y)
        place -= math.factorial(len(per)-1)*(x-y)
        i=len(nums)


# this is the code that worked:
# 
    # l1 = [i for i in range(10)]
    # l2 = [2,6,6,2,5,1,2,2]
    # l3 = []

    # for i in l2:
    #     l3.append(l1[i])
    #     l1.remove(l1[i])
    #     print(l3)

    # v2 works!