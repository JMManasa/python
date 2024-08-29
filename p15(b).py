#Write a program to swap two numbers 
#     b. without using a temporary variable
a=10;b=20
print(f"Before swapping:\na = {a}  b = {b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping:\na = {a}  b = {b}")
