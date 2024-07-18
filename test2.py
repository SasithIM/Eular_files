string = 'we45667788999jgdsdfvbngreq12edgju4'
while True:
    try:
        n=int(input(': '))
    except:
        break
    out = ''

    for i in string:
        out += chr(ord(i)-n)

    print(out)