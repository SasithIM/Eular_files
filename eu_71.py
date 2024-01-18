from fractions import Fraction
den = 10**6;minfr=0
for j in range(den,1,-1):
    for i in range(j,1,-1):
        if i/j < 3/7:
            x = Fraction(i,j)
            if x>minfr:
                print(x)
                minfr=x
            break


# it's the second one. No need to let it run till completion.
# maybe there's a better way. check later