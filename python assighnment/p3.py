b=[]
a = [int(x) for x in raw_input().split()]
for i in range(len(a)):
	if a[i] is 6:
		k=i
		f=k
		while(a[f]!=7):
			f += 1
			#print k
		p=f
b[:]=a[:k] + a[p+1:]
print sum(b)			
