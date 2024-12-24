#reversing words
s="An apple a day keeps the doctor away"
print(s)
l1=list(s.split())
l2=[]
for i in l1:
    l2.append(i[::-1])
s=" ".join(l2)
print(s)
