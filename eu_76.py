# target=
# def com_count(n):
#     count=0 ; nums=[i for i in range(1,n)] ; i=1
#     while True:
#         rest = target - n*i
#         if rest==0:
#             return count
#         for j in nums:
#             if not(rest%j):
#                 count+=1
#         i+=1
#         if n*i>target:
#             return count
# ways=1
# for i in range(2,target):
#     ways+=com_count(i)
#     print(i,com_count(i))
# print(ways)

