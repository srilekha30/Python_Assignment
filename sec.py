x=int(input())
y=input().split()
y=list(map(int,y))
a=max(y)
b=y.count(a)
#print (a)
#print (b)

for i in range(b):
	y.remove(a)
k=sorted(y)
print (k[-1])
