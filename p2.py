#Write a Python program to accept a filename from the user and print the extension of that file.
f=input()
c=0
for i in f:
    c+=1
    if i=='.':
        break
for j in range(c,len(f)):
    print(f[c],end='')
    c+=1
