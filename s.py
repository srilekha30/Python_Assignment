def print_formatted(number):
    x=" "
    for i in range(1,number+1):
        print (i,end=" ")
        print (oct(i)[2:],end=" ")
        print (hex(i)[2:].upper(),end=" ")
        print ((bin(i)[2:]))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
