"""def f(n):
	p=1
	for i in range(1,n+1):
		p=p*i
		return p"""
		
l=input()
def f(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def c(n,r):
	s=f(n)
	d=f(n-r)*f(r)
	z=s/d	
	return z


for x in range(0,l):
	for y in range(0,l-x):
        			
		print "", 
	        
	for y in range(0,x+1):
				
		z=c(x,y)
		print z,
	print
	

	
