class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("manasa",19)
print(getattr(p1,'name'))
print(getattr(p1,"age"))
setattr(p1,'age',40)
print(getattr(p1,'age'))
print(hasattr(p1,'id'))
print(hasattr(p1,"age"))
