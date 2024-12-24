#merge the 1st element of l1 with last of l2
l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
for i in range(len(l1)):
    if(l1[i]!=None and l2[len(l2)-i-1]!=None):
        print(l1[i]+l2[len(l2)-i-1],end=" ")
    else:
        if(l1[i]==None):
            print(l2[len(l2)-i-1],end=" ")
        else:
            print(l1[i],end=" ")

#method 2
print()
l2.reverse()
for i in range(len(l1)):
    if(l1[i]!=None and l2[i]!=None):
        print(l1[i]+l2[i],end=" ")
    else:
        if(l1[i]==None):
            print(l2[i],end=" ")
        else:
            print(l1[i],end=" ")
