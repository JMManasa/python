#dec-->oct and vice versa
d=int(input())
o=oct(d)
print(o)

o=o[2:]
dv=int(o,8)
print(dv)

#dec-->hexa and vice versa
d=int(input())
o=hex(d)
print(o)

o=o[2:]
dv=int(o,16)
print(dv)
