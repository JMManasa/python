# A cashier has currency notes of denominations 100’s, 50’s, 20’s, 10’s, 5’s, 2’s and 1’s. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
c=int(input("Input the amount: "))
h=c//100
c%=100
fy=c//50
c%=50
ty=c//20
c%=20
t=c//10
c%=10
f=c//5
c%=5
tw=c//2
c%=2
print("There are:")
print(f"{h} Note(s) of 100")
print(f"{fy} Note(s) of 50")
print(f"{ty} Note(s) of 20")
print(f"{t} Note(s) of 10")
print(f"{f} Note(s) of 5")
print(f"{tw} Note(s) of 2")
print(f"{c} Note(s) of 1")
