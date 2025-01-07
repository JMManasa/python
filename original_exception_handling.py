try:
    a,b=map(int,input().split())
    c=a/b
    print(c)
except:
    print("Given wrong input, give the correct innput\n2 chances left")
    chances=2
    while(chances):
        a,b=map(int,input().split())
        if(b==0):
            chances-=1
            if(chances==0):
                print("chances over")
                break
            print("Give the correct input\n",chances,"chances left")
            #continue
        else:
            c=a/b
            print(c)
            break
