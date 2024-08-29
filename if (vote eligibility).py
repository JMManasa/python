#without using else statement we can do if-else models by using exit() as shown above
#vote eligibility

a=int(input("Enter the age: "))
if(a<18):
    print("You are not eligible for voting")
    diff=18-age
    print("You have to weight {diff} years for voting.")
    exit()      #to terminate program
print("You are eligible for voting")



