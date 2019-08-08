"""def pro(k):
	if k==1:
		return 1*s[0]
	else:
		return s[k-1]*pro(k-2)"""

s = raw_input()
numbers = list(map(int, s.split()))
#print numbers
#k=len(numbers)
#print pro(k)
import operator
print reduce(operator.mul,numbers,1 )
