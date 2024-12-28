class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
    def decide(self):
        print("Major") if(self.age>=18) else print("Minor")
            
        
            

p1=Person("Manasa",10)
p2=Person("Moditha",19)

p1.display()
p1.decide()
p2.display()
p2.decide()
