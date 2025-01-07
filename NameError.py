a=[10,20,30]
print(a)
del a
try:
    print(a)
except:
    print("Name is not found")
