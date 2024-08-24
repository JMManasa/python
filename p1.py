#Write a python program to read 5 numbers from the user and find its sum and avg

n1=int(input("Enter the 1st Number: "))
n2=int(input("Enter the 2nd Number: "))
n3=int(input("Enter the 3rd Number: "))
n4=int(input("Enter the 4th Number: "))
n5=int(input("Enter the 5th Number: "))
s=n1+n2+n3+n4+n5
avg=s/5
print(f"Numbers are: {n1},{n2},{n3},{n4},{n5}")
print(f"Sum = {s}")
print(f"Average = {avg}")
print()

#other methods
#comma
print("Numbers are:",end=" ")
print(n1,n2,n3,n4,n5,sep=",")

#format
print("Numbers are: {},{},{},{},{}".format(n1,n2,n3,n4,n5))

#format specifiers
print("Numbers are: %d,%d,%d,%d,%d"%(n1,n2,n3,n4,n5))
