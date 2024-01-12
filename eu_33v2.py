from fractions import Fraction as fr
nu =1; de=1
for i in range(12,100):
    for j in range(i+1,100):
        x=i/j; s1= str(i); s2= str(j)
        if (i%10) and (j%10) and (i%11) and (j%11) and not(i==j) and not(int(x)==x):
            if s1[0]==s2[0]or s1[0]==s2[1]:
                s2=s2.replace(s1[0],''); s1 = s1[1]
            elif s1[1]==s2[0]or s1[1]==s2[1]:
                s2=s2.replace(s1[1],''); s1 = s1[0]
            else:
                continue
            if s1!='0' and (s2!='0' and s2!=''):
                if x == int(s1)/int(s2):
                    print(i,j,s1,s2)
                    nu*=i; de*=j
        else:
            pass
print(nu,de)
print(fr(nu,de))
