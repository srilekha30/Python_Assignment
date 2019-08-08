a=45
b=45
print id(a)
print id(b)
def func(x):
	print id(x)

func(a)

def func1(b):
	print id(b)

func1(b)

#if value is same and variable is diff.. still it points to same memory location-
