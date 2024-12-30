class A:
    def myname(self):
        print("I am a class A")

class B(A):
    def myname(self):
        print("I am a class B")

class C(A):
    def myname(self):
        print("I am a class C")

class D(B,C):
    pass

d=D()
d.myname()
print(D.__mro__)           #priority order
print(D.mro())          #priority order
