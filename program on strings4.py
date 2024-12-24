s="I$am*$a$do$c$#tor$"
count=0
for i in range(len(s)-2):
    if s[i]=="$" and s[i+2]=="$":
        count+=1
print(count)

