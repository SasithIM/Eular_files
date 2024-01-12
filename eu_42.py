def name_count(name):
    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    count = 0
    for i in name:
        count += alp.index(i)+1
    return count

cList = []; count=0

with open('0042_words.txt') as file1:
    for i in file1.read().split(','):
        x = (name_count(i.removeprefix('"').removesuffix('"')))
        y = ((2*x+0.25)**0.5)-0.5
        if not(y-int(y)):
            count+=1

print(count)