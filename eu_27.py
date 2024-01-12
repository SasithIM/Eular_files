import primes as pr

b_list = pr.primes(1001)
max_p,max_a,max_b = 0,0,0
for b in b_list[1::]:
    for a in range(-b+1,b-1):
        n=1
        while True:
            x = n**2+a*n+b
            if not(pr.is_prime(x)):
                break
            n+=1
            if n+1>max_p:
                max_p = n+1
                max_a = a; max_b = b

print(max_a,max_b,max_p,max_a*max_b)


### A test to check if true: ###

# while True:
#     try:    
#         a=int(input('a: '));b=int(input('b: '))
#     except:
#         continue
#     while True:
#         n = input("n('e' to exit,'b' to go back): ")
#         if n == 'e':
#             exit()
#         elif n == 'b':
#             break
#         else:
#             try:
#                 n = int(n)
#             except:
#                 continue
#             print(n**2+a*n+b)
