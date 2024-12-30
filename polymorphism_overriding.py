class bank:
    def getroi(self):
        return 10

class sbi(bank):
    def getroi(self):
        return 8

class icici(bank):
    def getroi(self):
        return 9

b1=bank()
s1=sbi()
i1=icici()
print(b1.getroi())
print(s1.getroi())
print(i1.getroi())


