#Print all the even numbers between the given range and also give a count.
print("Enter the range")
n1=int(input("Enter starting value: "))
n2=int(input("Enter ending value: "))
i=n1
c=0
while(i<=n2):
    if(i%2==0):
        print(i)
        c+=1
    i+=1
print("count:",c)
