class Person:
    static_count=0
    def __init__(self):     #non parameterized constructor
        Person.static_count+=1
        print(Person.static_count)

p1=Person()
p2=Person()
