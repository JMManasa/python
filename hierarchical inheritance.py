class Father:
    fname=""
    def father(self):
        print(self.fname)

class Child1(Father):
    cname=""
    def child1(self):
        print(self.fname,self.cname)

class Child2(Father):
    name=''
    def show(self):
        print(self.fname,self.name)


s1=Child1()
s2=Child2()

s1.fname="Bala"
s1.cname="Manasa"
s1.child1()

s2.fname="Bala"
s2.name="Theerdha"
s2.show()


