inp=input()
l=[]
str="ABCDEFG"
ans=0
c=0
for i in inp[::-1]:
    if(i in str):
        l.append(ord(i)-55)
    else:
        l.append(int(i))
for i in l:
    ans+=(17**c*i)
    c+=1
print(ans)
        
