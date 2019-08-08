def NodeCreate(value,next):
	return [value,next]

def NodeValue(n):
	return n[0]

def NodeNext(n):
	return n[1]

def NodeSetValue(n,value):
	n[0]=value
	return n
	

def NodeSetNext(a,b):
	a[1]=b
	return a
		
def ListCreate(*args):
	for i in range(0,len(args)):
		k= (NodeCreate(args[i],None))
		print (NodeValue(k))
		







a=NodeCreate(5,None)
b=NodeCreate(4,None)
print (NodeValue(a))
print (NodeNext(a)) 
print (a)
print (NodeValue(b))
print (NodeNext(b))
print (b)

"""print NodeSetValue(a,10)
print NodeSetNext(a,b)
print NodeSetNext(b,NodeCreate(6,None))
print NodeNext(a)
print (a)
print (b)
print NodeValue(a)
print NodeValue(NodeNext(b))"""
(ListCreate())
