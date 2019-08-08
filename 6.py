ph=input()
import sys
i=0
print ph[0].upper(),
sys.stdout.softspace=0
while i<len(ph):
	if ph[i]==" ":
		print ph[i+1].upper(),
		sys.stdout.softspace=0
	i=i+1
print "\n"
