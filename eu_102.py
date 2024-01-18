def area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2)

count=0
with open('0102_triangles.txt') as f1:
    for line in f1.readlines():
        line = [int(i) for i in line.split(',')]
        if area(*line) == area(0,0,*line[:4])+area(0,0,*line[2:])+area(0,0,*line[:2],*line[4:]):
            count+=1

print(count)