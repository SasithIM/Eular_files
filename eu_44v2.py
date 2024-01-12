lim = 10000 #there's only one at 1020 2167(probably)

def diff(x,y):
    return int(abs((x*(3*x-1)-y*(3*y-1))/2))

for x in range(1,lim):
    for y in range(x+1,lim):
        n_add = ((x*(3*x-1)+y*(3*y-1))/3+1/36)**0.5+1/6
        if not(n_add-int(n_add)):
            n_diff = ((abs(x*(3*x-1)-y*(3*y-1)))/3+1/36)**0.5+1/6
            if not(n_diff-int(n_diff)):
                print(diff(x,y))