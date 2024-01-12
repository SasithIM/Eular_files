with open('0059_cipher.txt') as file1:
    c_list = [int(i) for i in file1.read().split(',')]

alp = 'abcdefghijklmnopqrstuvwxyz'
alp = [ord(i) for i in alp]

for i in alp:
    for j in alp:
        for k in alp:
            key = [i,j,k]
            n=0; text = ''
            check = ''
            for l in c_list:
                x = l ^ key[n] 
                text+=chr(l ^ key[n])
                n += -2 if n==2 else 1
            if 'the' in text and 'and' in text and 'is' in text:
                print(text)
                print(sum([ord(i) for i in text]))
# too long can't know if a word or not