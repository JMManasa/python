d1={'name' : "Manasa",'rollno' : 576,'per' : 96.6}
print(len(d1))  #function
print("-------------------------------------------------------------")
#methods

'''To get keys'''
print(d1.keys())
print(*d1)
print("-------------------------------------------------------------")
'''To get values'''
print(d1.values())
#syntax - get(key, text if key is not present)
print(d1.get("name","NOT THERE"))
print(d1.get("branch","NOT THERE"))
#syntax - setdefault(key, text if key is not present)
print(d1.setdefault("rollno","NOT THERE"))
print(d1.setdefault("roll"))    #2nd parameter is optional
print(d1["per"])
print("-------------------------------------------------------------")
'''To get all items'''
print(d1)
print(d1.items())
for i,j in d1.items():
    print(i,j)

print("-------------------------------------------------------------")

#modifying dictionary

d1['branch']='CSE'      #adding another element at end
print(d1)
d2={'name' : "Moditha",'rollno' : 676,'per' : 86.6}
d1.update(d2)
print(d1)

print("-------------------------------------------------------------")

#deleting records/elements

del d1['roll']      #removing particular item
print(d1)

d1.popitem()  #removes last item
print(d1)

d1.pop("rollno")      #removing particular item
print(d1)

d1.clear()
print(d1)       #{}
'''
del d2
print(d2)       #name error
'''
print("-------------------------------------------------------------")

d1={'name' : "Manasa",'rollno' : 576,'per' : 96.6}
d2={'name' : "Moditha",'rollno' : 676,'per' : 86.6}
'''
print(d1+d2)    #error (also error in set)
print(d1*3)       #error (also error in set)
'''
print("-------------------------------------------------------------")

#copy operation

d2=d1
print(d1)
print(d2)
print(id(d1))
print(id(d2))

d2=d1.copy()
print(d1)
print(d2)
print(id(d1))
print(id(d2))

import copy    #module
d2=copy.copy(d1)
print(d1)
print(d2)
print(id(d1))
print(id(d2))

print("-------------------------------------------------------------")

print(dir(dict))

print("-------------------------------------------------------------")

#dict.fromkeys(keys,values)
