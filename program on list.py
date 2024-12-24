l1=[11,8,23,7,25,15]
l2=[6,33,50,31,46,78,16,34]
l3=[]
for i in l1:
    if 2*i in l2:
        l3.append(i)
print(l3)
