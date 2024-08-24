#Write a python program to read a number n from the user and compute n+nn+nnn
#input=5  output=615   (5+55+555)
#input=20 output=204060 (20+2020+202020)
n=(input("Enter a number n: "))
print("The value is:",int(n)+int(n+n)+int(n+n+n))
