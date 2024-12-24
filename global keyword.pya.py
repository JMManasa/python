def fun():
    global a                #if global not used,
    a=a*2                   #UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    print(a,id(a))

a=5
print(a,id(a))
fun()
print(a,id(a))
