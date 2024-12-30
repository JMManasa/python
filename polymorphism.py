class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,o):
        return self.a+o.a

obj1=A(1)           
obj2=A(2)           #control goes to 5th line
obj3=A("Geeks")
obj4=A("For")
print(obj1+obj2)
print(obj3+obj4)
