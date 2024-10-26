nor_v=300.0
nor_nv=400.0
del_v=600.0
del_nv=800.0
ec=100.0
et=100.0
wb=20.0
kp=5.0
sd=75.0
ta=20.0
bill=0
print("Pizza categories")
print("1.Normal Pizza\n2.Deluxe Pizza")
print()
pc=int(input("Enter your choice(1 or 2):"))
if(pc==1 or pc==2):
    print("Pizza Types\n1.Veg\n2.Non Veg")
    print()
    pt=int(input("Enter your choice(1 or 2):"))
if(pc==1):
    if(pt==1):
        bill+=nor_v
    elif (pt==2):
        bill+=nor_nv
    else:
        print("invalid value")
        exit()
elif(pc==2):
    if(pt==1):
        bill+=del_v
    elif (pt==2):
        bill+=del_nv
    else:
        print("invalid value")
        exit()
else:
    print("invalid value")
    exit()
base=bill
c=int(input("Extra Cheese? [1.Yes or 2.NO]: "))
if c==1:
    bill+= ec 
t=int(input("Extra Topping? [1.Yes or 2.NO]: "))
if t==1:
    bill+= et 
w=int(input("Do you want Water Bottles? [1.Yes or 2.NO]:"))
if w==1:
    n1=int(input("How many Bottles? : "))
    bill+=(n1*wb) 
k=int(input("Do you want Ketchup? [1.Yes or 2.NO]: "))
if k==1:
    n2=int(input("How many Packets? : "))
    bill+=(n2*kp)
d=int(input("Do you want Soft Driknks? [1.Yes or 2.NO]: "))
if d==1:
    n3=int(input("How many cans? : "))
    bill+=(n3*sd)
take=int(input("Is it a Take Away? [1.Yes or 2.NO]:"))
bill+= ta if take==1 else 0
gst=bill*0.18
print()
print("---------------------------------")
print("*****Pizza Bill Generator*****")
print("---------------------------------")
print(f"Base Price                = {base}")
if(c==1):
    print(f"Extra Cheese            = {ec}")
if(t==1):
    print(f"Extra Toppings          = {et}")
if(w==1):
    print(f"Water Bottle            ={n1*wb}")
if(k==1):
    print(f"Ketchup Packets         = {n2*kp}")
if(d==1):
    print(f"Soft Drinks             ={n3*sd}")
if(take==1):
    print(f"Take Away Charges       = {ta}")
print(f"-----------------------------------------")
print(f"Total Cost                 = {bill}")
print(f"GST Charges                = {gst}")
print(f"-----------------------------------------")
print(f"Net Amount Payable         = {bill+gst}")







