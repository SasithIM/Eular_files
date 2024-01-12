from fractions import Fraction as fr
start = fr(1)
for i in range(12,100):
    for j in range(12,100):
        x = i/j; s1 = str(i); s2 = str(j)
        if not(j%10) or not(i%10) or (i==j) or (int(x)==x) or s1[0]==s1[1] or s2[0]==s2[1]:
            continue
        else:
            for k in s1:
                if k in s2:
                    s1=s1.replace(k,''); s2=s2.replace(k,'')
                    break
            if x == int(s1)/int(s2):
                print(fr(x),i,s1,j,s2)
                start *= x
            

print(fr(start))