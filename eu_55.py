def is_palindrome(num):
    return str(num) == str(num)[::-1]



count=0
lychrel = []

for i in range(1,10000):
    num = i
    for j in range(50):
        num+=int(str(num)[::-1])
        if is_palindrome(num):
            # print(i,j)
            break
    else:
        count+=1#;lychrel.append(i);print(i,j,'ly',count)

print(count)
# for i in lychrel:
#     num = i;print(i,end=',')
#     for j in range(50):
#         if is_palindrome(num):
#             break
#         else:
#             num+=int(str(num)[::-1]);print(num,end=',')
#     print('\n')