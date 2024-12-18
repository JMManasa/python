def a(st1,st2):
    print(st1)
    print(b(st2))      #calling other function  'b"

def b(st2):
    return st2.upper()

a("hello","world")
