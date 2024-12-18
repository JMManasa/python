def cbr(a):         #call by reference
    print(a,id(a))
    a.append("cse")
    print(a,id(a))

a=["rise"]
print(a,id(a))
cbr(a)


#The address is same for all
