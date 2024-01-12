num_list = {4,}

for i in range(2,101):
    for j in range(2,101):
        num_list.add(i**j)

print(len(sorted(list(num_list))))