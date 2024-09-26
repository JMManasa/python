#write a python program to read a number from the user and find the factors of it and also find it's sum
n=int(input())
i=1
s=0
while(i<=n):
    if(n%i==0):
        print(i)
        s=s+i
    i=i+1
print(s)

#simplified way

n=int(input())
print(1)
i=2
s=0
while(i<=n/2):
    if(n%i==0):
        print(i)
        s=s+i
    i=i+1
print(n)
print(1+n+s)
