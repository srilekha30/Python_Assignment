var=raw_input()
i=0
l=0
var=var.upper()
while i<len(var):
     if var[i]!=" ":
     
            l=l+ ord(var[i])-64
        
     i=i+1
     
print l
