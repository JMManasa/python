#Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. 
#Write a Python program to calculate his gross salary.
b=float(input("Enter the Basic Pay: Rs."))
da=b*0.4
hra=b*0.2
g=b+da+hra
print(f"Basic Salary:			Rs.{b:.2f}")
print(f"Dearness Allowance:		Rs.{da:.2f}")
print(f"House Rent Allowance:	         Rs.{hra:.2f}")
print(f"Gross Pay is 			Rs.{g:.2f}")
