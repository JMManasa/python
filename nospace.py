def nospace(s):
    str=""
    list=s.split()
    for i in list:
        str+=i
    return str
        

s=input()
str=nospace(s)
print(str)
