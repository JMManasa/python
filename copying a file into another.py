import sys
inf=open(sys.argv[1],'r')
ouf=open(sys.argv[2],'w')
r=inf.read()

while r:
    ouf.write(r)
    r=inf.read()


print("File copied!")
inf.close()
ouf.close()
