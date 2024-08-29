#Write a program to find the sum of the digits of a three-digit number. If the givennumber is more than 3 digits ignore the rest.
n=int(input("Enter a 3-digit  number: "))
s=0
while(n>1000):
    n=n//10
for i in range(3):
    r=n%10
    s=s+r
    n=n//10
print(s)
