from math import sqrt

maxx = 0
for d in range(1000):
    if (sqrt(d)-int(sqrt(d))):
        x,y = 1,1
        while True:
            x = sqrt(1+d*(y*y))
            if not(x-int(x)):
                break
            y+=1;print(d,y)
        if x>maxx:
            maxx=x
print(maxx)


#takes waayyy too long. might need a different way to solve