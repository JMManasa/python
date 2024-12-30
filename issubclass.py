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
print(issubclass(Derived,Add))
print(issubclass(Derived,Multiply))
print(issubclass(Add,Multiply))
