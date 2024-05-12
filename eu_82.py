matrix=[]
with open('0082_matrix.txt') as f1:
    for line in f1.readlines():
        matrix.append([int(i) for i in line.split(',')])
for i in matrix:
    i.append(float('inf'))
matrix.append([float('inf')]*81)

for col in range(1,80):
    for row in range(80):
        matrix[row][col+1]

# print(matrix)