def swap_case(s):
	for i in s:
		if i.isupper:
			i=i.lower()
		elif i.islower:
			i=i.upper()
	return s


s=input()
print (swap_case(s))
