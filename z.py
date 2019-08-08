import math
x=complex(input())
k=x.imag/x.real
l=-1*(x.imag/abs(x.real))
m=abs(x.imag)/abs(x.real)
if(x.real>0 and x.imag>0):
    print (round(math.sqrt(x.real*x.real+x.imag*x.imag),3))
    print (round(math.atan(k),3))
if(x.real>0 and x.imag<0):
    print (round(math.sqrt(x.real*x.real+x.imag*x.imag),3))
    print (round(-1*(math.atan(k)),3))
if(x.real<0 and x.imag>0):
    print (round(math.sqrt(x.real*x.real+x.imag*x.imag),3))
    print (round(-1*(math.atan(l)),3))
if(x.real<0 and x.imag<0):
    print (round(math.sqrt(x.real*x.real+x.imag*x.imag),3))
    print (round(math.atan(m),3))
