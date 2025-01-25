s="ZOHOCORPORATIONTEAM"
i=0
while(i<7):
    print(s[i],end=" ")
    i+=1
print()
for j in range(5):
    print(" ",end=" ")
    for k in range(5-j):
        if(k==4-j):
            print(s[i],end=" ")
            i+=1
        else:
            print(" ",end=" ")
    print()
while(i<len(s)):
    print(s[i],end=" ")
    i+=1
