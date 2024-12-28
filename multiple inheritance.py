class Father:
    fname=""
    def father(self):
        print(self.fname)

class Mother():
    mname=""
    def mother(self):
        print(self.mname)

class child(Father,Mother):
    cname=''
    def show(self):
        print(self.fname,self.mname,self.sname)


s1=child()
s1.fname="Bala"
s1.mname="Visali"
s1.sname="Manasa"
s1.show()
s1.father()



