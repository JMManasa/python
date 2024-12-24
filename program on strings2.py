s="madam said wow"
print(s)
l=list(s.split())
p=0
n=0
for i in l:
    if i==i[::-1]:
        p=p+1
    else:
        n=n+1
print("No. of palindrome words are:",p)
print("No. of not palindrome words are:",n)

    
