class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)

p1=Person("Manasa",19)
p2=Person("Moditha",19)

p1.display()
p2.display()

del p1.name     #deleting an attribute of an obj

del p1          #deleting total obj
p1.display()
