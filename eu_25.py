
seq = [1,1]; i = len(seq)
while i < 1000:
    x = seq[-1] + seq[-2]
    seq.append(x)
    i = len(str(x))
print(len(seq))
