a=[0,1,2,3,4,5,6,7,8,9]
b=[]
count=0
i=0
while i<10:
	
	count=count+a[i]
	i+=2
print count
i=0
while i<10:
	if(i%2==0):
		b.append(a[i])
	i+=1
print b
