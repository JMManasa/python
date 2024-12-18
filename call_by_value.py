def cbv(a):               #call by value
    print(a,id(a))
    a=a+1
    print(a,id(a))                       #only this changes

a=5
print(a,id(a))
cbv(a)
print(a,id(a))


#The address is same up to data is not changed
#once the data is changed, there exsist a seperate copy i.e, diff address
#but after calling function, data will be as before
