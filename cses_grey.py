x = [[0], [1]]
n = int(input())

for i in range(n - 1):
    a = [[0] + m[:] for m in x]
    b = [[1] + m[:] for m in x[::-1]]
    x = a + b
for i in x:
    print(''.join(map(str,i)))
