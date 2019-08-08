x=input()
c=0
i=1
for i in range(1,x):
	if (x%i==0):
		c=c+i
if(c==x):
	print "perfect number"
else:
	print "not a perfect number"

