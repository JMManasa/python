#Consider that you have purchased a Laptop – price get it from the user upon which a sales tax of 6% is applied. Write a Python program that calculates and displays the total purchase price of the Laptop.
c=float(input("Enter the price of the Laptop: "))
c=c+(0.06*c)    #adding 6% sales tax
print("Total Cost Price of the Laptop is %.2f"%(c))
