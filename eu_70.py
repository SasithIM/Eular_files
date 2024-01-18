# Python3 program to calculate 
# Euler's Totient Function
def totient(n):
	
	# Initialize result as n
	result = n; 

	# Consider all prime factors
	# of n and subtract their
	# multiples from result
	p = 2; 
	while(p * p <= n):
		
		# Check if p is a 
		# prime factor.
		if (n % p == 0): 
			
			# If yes, then 
			# update n and result
			while (n % p == 0):
				n = int(n / p)
			result -= int(result / p)
		p += 1

	# If n has a prime factor
	# greater than sqrt(n)
	# (There can be at-most 
	# one such prime factor)
	if (n > 1):
		result -= int(result / n)
	return result


r = float('inf');n=0
for i in range(2,10**7):
    t=totient(i)
    if sorted(str(i))==sorted(str(t)):
        print(i,i/t,r)
        if i/t<r:
            r=i/t
            n=i
			
print(n,r)