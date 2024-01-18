# def count_sqrs(a,b):
#     count=0
#     for n in range(a-1,-1,-1):
#         for m in range(b-1,-1,-1):
#             count+=(a-n)*(b-m)
#     return count

def count_sqrs2(a,b):
    return int((a*(a+1)*b*(b+1))/4)

i=1;max_count=0;maxab=[]
while i<2001:
    j=1
    count1=0
    while True:
        x=count_sqrs2(i,j)
        if x>2*10**6:
            break
        count1=x
        j+=1
    if count1>max_count:
        max_count=count1
        maxab=[i,j-1]
    i+=1

print(max_count,maxab)

# print(count_sqrs2(36,77))