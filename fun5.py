#x acts as tuple (default)
def frmv(x,y):            #funtion return multiple values                                   
    return x+y,x-y
    
a,b=int(input()),int(input())
x=frmv(a,b)           #calling fuction                                     
print(x)                                                                                   




#x acts as set
def frmv(x,y):            #funtion return multiple values                                     
    return {x+y,x-y}
    
a,b=int(input()),int(input())
x=frmv(a,b)           #calling fuction                                     
print(x)                                                                                   


  

#x acts as list
def frmv(x,y):            #funtion return multiple values                                      
    return [x+y,x-y]
    
a,b=int(input()),int(input())
x=frmv(a,b)           #calling fuction                                    
print(x)                                                                                  





#x acts as dict
def frmv(x,y):            #funtion return multiple values                                      
    d={}
    d['add']=x+y
    d['sub']=x-y
    return d
    
a,b=int(input()),int(input())
x=frmv(a,b)           #calling fuction                                    
print(x)                                                    
















