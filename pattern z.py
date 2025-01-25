s="ZOHOCORPORATIONTEAM"
c=0
for i in range(7):
    for j in range(7):
        if(i==0 or i+j==6 or i==6):
            print(s[c] ,end=" ")
            c+=1
        else:
            print(" ",end=" ")
    print()
    
