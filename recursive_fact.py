#find factorial
def fact(x):
    if(x>1):
        return x*fact(x-1)   #recursive call
    else:
        return 1
x=int(input())
print(fact(x))
