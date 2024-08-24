#Write a Python program that reads a floating-point number and then display the right-most digit of the integral part of the number.
f=float(input("Enter a Floating-point Number: "))
r=int(f)%10
print(f"Right-most Number is {r}")
