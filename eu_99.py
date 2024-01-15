import math
# def check(num1,num2):
#     if (num1[0]-num2[0])**num1[1]-num2[0]**(num2[1]-num1[1])>0.0:
#         return True
#     else:
#         return False

def check2(num1,num2):
    if(num1[1]*math.log(num1[0])-num2[1]*math.log(num2[0])>0):
        return True
    else:
        return False

lines=[]
with open('0099_base_exp.txt') as f1:
    for line in f1.readlines():
        lines.append([int(i) for i in line.split(',')])    

max_line = 1
for i in range(1,len(lines)):
    if(check2(lines[i],lines[max_line-1])):
        max_line=i+1
    else:
        pass

print(max_line)