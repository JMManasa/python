def cse1():
    a=5                 #local variable
    print("a: ",a,id(a))
    print("b: ",b,id(b))
def cse2():
    a=10              #local variable
    print("a: ",a,id(a))
    print("b: ",b,id(b))

b=20                  #global variable
print("b: ",b,id(b))
cse1()
cse2()

