nh=144
while True:
    h = nh*(2*nh-1)
    p = (2*h/3 + 1/36)**0.5 + 1/6
    # t = (2*h+0.25)**0.5 + 1/2
    if (not(p-int(p))):
        print(h)
        break
    nh+=1