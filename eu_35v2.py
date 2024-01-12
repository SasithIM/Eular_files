import primes

prime_list = primes.primes(10**6)
prime_set = set(prime_list)
i=0;count=0

while i < len(prime_list):
    s = str(prime_list[i]);c=0;l=len(s)
    for i in range(l):
        n = int((s[i:]+s[:i]))#;print(n,end=' ')
        if n in prime_set:
            c+=1
            prime_set.remove(n)
            prime_list.remove(n)
    if s[:l//2]==s[l//2:] and l>1:
        c+=1
    if c == len(s):
        count+=c;print(s,'+'*c)
    i+=1
print(count)

# nope!