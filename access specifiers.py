class base:
    def __init__(self):
        self._a=32       #protected

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a)

b1=base()
d1=derived()
print(b1._a)
