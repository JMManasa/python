#random numbers with required no.of digits
import random
n=int(input())
i=1
while i<=n:
    print(random.randint(0,9),end="")
    i+=1
