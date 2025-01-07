try:
    a,b=map(int,input().split())
    c=a/b
    print(c)
    '''
except Exception as e:
    print("Can't divide with Zero")
    print(e)
    '''

except (ArithmeticError,ValueError):
    print("Can't divide with Zero or given other than integer")
 
else:
    print("HI I am else block")
print("Line after an exception will not executes if it is not handled")
