from math import sqrt

max_y=0
for i in range(1,1001):
    x=sqrt(i)
    if x-int(x):
        j=1
        while True:
            if not(sqrt(1+i*j**2)%1):
                y=sqrt(1+i*j**2)
                if y>max_y:
                    max_y=y
                break
            j+=1
            print(i,j)
    print(i,'\n')

print(max_y)