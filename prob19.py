day_p_mon = [31,28,31,30,31,30,31,31,30,31,30,31]
day_p_mon_long = [31,29,31,30,31,30,31,31,30,31,30,31]
x = []
arr = [0]

for year in range(1901,2001):
    if (year%4 == 0) and (not year%100 == 0 or year%400 == 0):
        x = day_p_mon_long
    else:
        x = day_p_mon
    
    for i in range(len(x)):
        arr.append(arr[-1] + x[i])
    
m = [ n for n in arr if n%7 == 0]

print(len(m))