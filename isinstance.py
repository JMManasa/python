class Add:
    def Summation(self,a,b):
        return a+b

class Multiply:
    def Multiplication(self,a,b):
        return a*b

class Derived(Add,Multiply):
    def divide(self,a,b):
        return a/b

d=Derived()
print(isinstance(d,Add))
print(isinstance(d,Multiply))
print(isinstance(d,Derived))

