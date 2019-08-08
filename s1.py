if __name__ == '__main__':
    s = input()
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    if(s.isalnum()==True):
        print (True)
        print (True)
        print (True)
        for i in s:
            if(i.islower()==True):
                c1=c1+1
        if(c1>0):
            print (True)
        else:
            print (False)
        for i in s:
            if(i.isupper()==True):
                c2=c2+1
        if(c2>0):
            print (True)
        else:
            print (False)
    elif(s.isalnum()==False):
        print (False)
        for i in s:
            if(i.isdigit()==True):
                c3=c3+1
        if(c3>0):
            print (True)
        else:
            print (False)
        for i in s:
            if(i.isalpha()==True):
                c4=c4+1
                if(i.islower()==True):
                    c5=c5+1
                if(i.isupper()==True):
                    c6=c6+1
            else:
                print (False)
           
        if(c4>0):   
            print (True)
        else:
            print (False)
        if(c5>0):
            print (True)
        else:
            print (False)
        if(c6>0):
            print (True)
        else:
            print (False)
        
    
