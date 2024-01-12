cube_dict={}
for i in range(1,10000) :
    id = ''.join(sorted(i for i in str(i**3)))
    if id in cube_dict:
        cube_dict[id].append(i)
        if len(cube_dict[id])==5:
            print(cube_dict[id],cube_dict[id][0]**3)
    else:
        cube_dict[id]=[i]
else:
    print('n too low')
# print([i**3 for i in cube_dict[id]])