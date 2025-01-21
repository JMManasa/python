s=input("Enter a Sentence: ")
l=s.split()
maxl=0
for i in l:
    if(i==i[::-1]):
        if(len(i)>maxl):
            maxl=len(i)
print(maxl)
f=1
for i in range(1,maxl+1):
    f*=i
print(f)
