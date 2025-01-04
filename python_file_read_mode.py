x=open('pfiles.txt','r')
#only one operation will execute at a time


content=x.read()
print(content)

content=x.read(6)
print(content)

content=x.readline()
print(content)

content=x.readline(6)
print(content)

content=x.readlines()
print(content)

content=x.readlines(6)
print(content)

#read operation without any operation
lines_count=0
for i in x:         #executes no.of lines times
    print(i)
    lines_count+=1
print("\nNo.of lines:",lines_count)

x.close()


