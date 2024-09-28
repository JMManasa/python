account_holder=input("Enter name of the account holder: ")
l=[]
print(f"Opening your account {account_holder}\n\tWelcome!")
#balance=input("Enter balance amount")
balance=0
for i in range(7):
    deposit=int(input("Enter the amount to deposit: "))
    l.append(deposit)
    balance+=deposit
print("deposited amounts are",l)
print(f"The Total Balance is {balance}/-")
withdraw=int(input("Enter amount to withdraw: "))
balance-=withdraw
print(f"The Total Balance is {balance}/-")
print(f"Closing your account {account_holder}\n\tThank you!")
    
    
