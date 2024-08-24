#Write a Python program to read the total number of seconds from the user and convert it into the following format – Hours:Minutes:Seconds
s=int(input("Input seconds: "))
h=s//3600
s=s%3600
m=s//60
s=s%60
print(f"H:M:S - {h}:{m}:{s}")
