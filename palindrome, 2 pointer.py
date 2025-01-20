s =list(map(int,input("numbers:").split()))
key=int(input("Enter key:"))
a=0
b=len(s)-1
c=0
while a<=b:
    c+=1
    if s[a]==key or s[b]==key:
        print("found")
        break
    a+=1;b-=1
print(c)
