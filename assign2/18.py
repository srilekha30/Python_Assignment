x=raw_input()
i=0
for i in x:
	if x.count(i)>1:
		print i,x.count(i)
		x=x.replace(i,"")
