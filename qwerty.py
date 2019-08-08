n,m=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
#A={input().split(" ")}
A={}
B={}
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))

A=set(l1)
B=set(l2)

count=0

for i in l:
	if i in A:
		count=count+1
	if i in B:
		count=count-1
print (count)
