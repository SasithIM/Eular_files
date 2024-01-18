def bouncy(num):
    num=str(num)
    l=len(num);s=''
    y=int(num[1])-int(num[0])
    if y==0:
        prs=''
    elif y<0:
        prs='d'
    else:
        prs='i'

    for i in range(1,l-1):
        x=int(num[i+1])-int(num[i])
        if x==0:
            continue
        elif x>0:
            s = 'i'
        else:
            s='d'
        if prs!='' and prs!=s:
            return True
        prs = s
        

i=100;count=0

while True:
    if bouncy(i):
        count+=1
    if count == 0.99*i:
        print(i,count)
        break
    i+=1

# with open('bouncy.txt','w') as f1:
#     for i in range(100,539):
#         # if bouncy(i):
#         #     count+=1
#         f1.write(f'{i},{bouncy(i)}\n')

# for i in range(100,21781):
#     if bouncy(i):
#         count+=1
# print(count*100/i,count)