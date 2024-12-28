import sys
sys.setrecursionlimit(50)
def num():
    global i
    print(i)
    i+=1
    num()

i=1
num()
