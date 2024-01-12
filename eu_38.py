full_str = [str(i) for i in range(1,10)]
pan_list = []
for i in range(1000000):
    con_str = '';j=1
    while len(con_str)<9:
        con_str+=str(i*j)
        j+=1
    if sorted(con_str) == full_str:
        pan_list.append(f'{con_str} {j}')

print(sorted(pan_list))