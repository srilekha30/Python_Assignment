var=raw_input()
i=0
l=0
var=var.upper()
#print var
while i<len(var):
	if var[i]!=" ":
		#print ord(var[i])-64
		l=l+ ord(var[i])-64
	"""if var[i]==" ":
		l=l-4"""
	i=i+1
	
print l
