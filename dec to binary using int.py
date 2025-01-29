#decimal-->binary and vice versa
d=int(input())
b=bin(d)
print(b)

b=b[2:]
dv=int(b,2)
print(dv)
