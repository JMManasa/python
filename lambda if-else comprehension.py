#finding max
a,b=map(int,input().split())
max=lambda a,b: a if(a>b) else b
print(max(a,b))

#finding palindrome or not
s=input()
palindrome=lambda s:print("Palindrome") if (s==s[::-1]) else print("Not palindrome")
palindrome(s)
