#Write a program to calculate the surface area of a cylinder given its radius and height.
r=int(input("Enter radius of the cylinder: "))
h=int(input("Enter height of the cylinder: "))
s = 2 * 3.14 * r * (r+h)
print(s)
