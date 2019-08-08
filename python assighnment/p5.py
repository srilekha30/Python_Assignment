def check(n):
	add=0
	while n>0:
		add += n%10
		n = n/10
	z=add	
	if z <10:
		return z
	elif z >= 10:
		f=check(z)
		return f		
k = int(input())
h = check(k)
if h < 10:
	if h == 7:
		print "The number is a lucky number"
	else:
		print "The number is not a lucky number"

	

