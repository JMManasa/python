x=open('pfiles.txt','rb')

position=x.tell()
print(position)

x.seek(13,0)
#print(x.read())

x.seek(2,1)
#print(x.read())

x.seek(-10,2)
print(x.read())
x.close()
