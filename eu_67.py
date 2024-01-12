triangle = []
with open("0067_triangle.txt") as file1:
    for line in file1.readlines():
        triangle.append([int(num) for num in line.split(' ')])


for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        triangle[i][j]+= max(triangle[i+1][j],triangle[i+1][j+1])

print(triangle[0][0])