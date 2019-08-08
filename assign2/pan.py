l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x=raw_input()
x=x.lower()
p=list(x)
flag=0
print p
for i in range(len(p)):
	if(p[i] in l):
		flag=flag+1
		l.remove(p[i])
	else:
		break
if(flag==26):
	print "pangram"
else:
	print "not a pangram"
