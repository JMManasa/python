#write a python program to read a number from user and find the sum of the digits
#using strings
n=input()
i=0;s=0
while i<len(n):
    s=s+int(n[i])
    i+=1
print(s)

s=0
#using math
n=int(input())
while n!=0:
    r=n%10
    s+=r
    n//=10
print(s)

    
