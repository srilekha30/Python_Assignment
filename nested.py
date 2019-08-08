x=int(input())
l=[]
#p=[]
for i in range(x):
	p=[]
	k=input()
	m=int(input())
	p.append(k)
	p.append(m)
	l.append(p)
print (l)

#l=sorted(l)


l.sort(key=lambda x: x[-1])


print(l)
