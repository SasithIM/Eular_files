n=1001
big = n**2
total = 0
step = n-1
while big >= 0 and step>0:
    for i in range(4):
        total += big;print(big)
        big-=step
    step-=2
print(total+1)