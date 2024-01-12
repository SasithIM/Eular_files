matrix=[]
with open('0081_matrix.txt') as f1:
    for line in f1.readlines():
        matrix.append([int(i) for i in line.split(',')])
for i in matrix:
    i.append(float('inf'))
matrix.append([float('inf')]*81)

for i in range(1,80):
    for j in range(0,i+1):
        matrix[i-j][j]+=min(matrix[i-j-1][j],matrix[i-j][j-1])
        
for i in range(80):
    for j in range(79,i,-1):
         matrix[j][80-j+i]+=min(matrix[j][80-j-1+i],matrix[j-1][80-j+i])
print(matrix[79][79])