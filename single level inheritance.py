#Ex 1:
class father:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class child(father):
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

obj1=father("Bala")
obj1.display()

obj2=child("Manasa")
obj2.show()

obj2.display()       #inheritance

#Ex 2:
class base:
    def __init__(self):
        self._a=32       #protected

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a)

d1=derived()
