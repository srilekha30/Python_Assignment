import sys
def convertToNumber():
	result=[]
	for i in range(1,len(sys.argv)):
		result.append(float(sys.argv[i]))
	return result


def main():
	ints=convertToNumber()
	print ("original",sys.argv)
	print ("after",ints)
main()
