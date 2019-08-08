x=raw_input()
i=0
c=0
d=0
for i in x:
	if i.isupper():
		c=c+1
	elif i.islower():
		d=d+1
print c
print d
