try:
    fileptr=open("abc.txt",'r')
    fileptr.write("Hi abc")
except:
    print('Wrong operation')
else:
    print('mode of the file is read')
finally:
    print("file closed")
    print("Error")
