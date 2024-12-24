#print high to low values
def display(a,b):
    if(a>=b):
        print(a)
        display(a-1,b)     #recursive call

a=int(input())
b=int(input())
display(a,b)
