s=input("String: ")
v=0
f=1
l="aeiou"
for i in s:
    if(i.lower() in l):
        v+=1
print(v)
for i in range(1,v+1):
    f*=i
print(f)
