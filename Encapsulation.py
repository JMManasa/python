class Base:
    def __init__(self):
        self.__a=32
        print(self.__a)


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print(self.__a)

#d1=Derived()
b1=Base()
#print(b1.a)


#there is encapsulation, because constructor, a are inside a class because of which security is provided
#only a can be used within the class, not in the child class or other part of program
