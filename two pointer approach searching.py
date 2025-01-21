l=list(map(int,input("List: ").split()))
t=int(input("Target :"))
a=0
b=len(l)-1

while a<=b:
    if(l[a]==t):
        print(a)
        break
    if(l[b]==t):
        print(b)
        break
    a+=1;b-=1
if(a>b):
    print("Not found")
