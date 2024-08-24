#Write a Python program to convert specified days into years, weeks and days.
#Note: Ignore leap year.
d=int(input("Enter the number of Days: "))
y=d//365
d=d%365
w=d//7
d=d%7
print(f"Years: {y}\nWeeks: {w}\nDays: {d}")
