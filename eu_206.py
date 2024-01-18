
n=1058921220
while True:
    y=n*n
    s=''
    if not(y%10):
        x=str(y)
        if x[::2]=='1234567890':
            print(n)
            break
    n+=1