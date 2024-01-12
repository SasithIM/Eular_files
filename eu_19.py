def year(yr,first_sunday):
    days = 365
    global leap
    leap = False
    if not(yr%100):
        if not(yr%400):
            days +=1;leap = True
    elif not(yr%4):
        days += 1;leap = True
    else:
        leap = False
    year = [False]*days
    year[first_sunday-1::7] = [True]*((days-first_sunday)//7+1)
    return year

def count_sundays(yr):
    all_sundays = sum(yr)
    months1 = [31,28,31,30,31,30,31,31,30,31,30]
    months2 = [31,29,31,30,31,30,31,31,30,31,30]
    if leap:
        for i in range(12):
            yr[sum(months2[:i:])] = False
            # print(yr[sum(months2[:i]):sum(months2[:i+1])],'\n')
    else:
        for i in range(12):
            yr[sum(months1[:i:])] = False
            # print(yr[sum(months1[:i]):sum(months1[:i+1])],'\n')

    monthfirst_sundays = all_sundays - sum(yr)
    return monthfirst_sundays
    # return yr

first_sunday1 = 6; year_num = 1901; count = 0

while year_num < 2001:
    year_arr = year(year_num,first_sunday1)
    new =  count_sundays(year_arr)
    count += new
    year_num += 1
    if leap:
        first_sunday1 -= 2
    else:
        first_sunday1 -= 1
    if first_sunday1 < 1:
        first_sunday1 += 7

print(count)