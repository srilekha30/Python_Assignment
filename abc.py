from itertools import combinations

s,k=input().split(" ")
y=int(k)

for i in range(1,y+1):
	l=sorted([''.join(x) for x in combinations(s,i)])
	for j in l:
		print (j)
