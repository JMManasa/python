#guest list manager app
guest_list=[]
print("Welcome to the guest list manager app")
while True:
    print("1.Add a new guest ")
    print("2.View the guest List")
    print("3.Delete a guest")
    print("4.Guest list in alphabetical order")
    print("5.Search for a guest")
    print("6.Update guest name")
    print("7.No.of guests in guest_list")
    print("8.Quit")
    opt=int(input("Enter your choice(1-8): "))
    match opt:
        case 1:
            guest_list.append(input("Enter new guest: "))
            print("Successfully added")
        case 2:
            for i,v in enumerate(guest_list):
                print(f"{i+1}\t{v}")
        case 3:
            s = input("Do you want to delete based on \na. Value\nb.Position\nYour Choice [a/b]: ").lower()
       
        match s:
            case 'a':
                # value based deletion
                name = input("Enter the Guest Name to be removed: ")
                # Checking whether the name is present in the List
                if name in guest_list:
                    guest_list.remove(name)
                    print(F"{name} has been successfully removed")
                    print()
                else:
                    print(F"{name} is not present in the Guest List")
                    print()

            case 'b':
                # index based deletion
                x = int(input("Enter the Position Number to delete: "))
                # Checking if the given position number is valid
                if x <= len(guest_list):
                    x=x-1
                    name = guest_list.pop(x)
                    print(F"{name} has been deleted successfully")
                    print()
                else:
                    print("Invalid Position Entered. Pls view the data and enter a number correctly")
                    print()

            case _: print("Invalid Option")
        case 4:
            sorted_list=sorted(guest_list)
            for i,v in enumerate(sorted_list):
                print(f"{i+1}\t{v}")
        case 5:
            n=input("Enter guest to search: ")
            if n in guest_list:
                print(f'{n} is in guest_list at {guest_list.index(n)+1}')
            else:
                print(f'{n} is not in guest_list')
                ans=(input("Do you want to add this name ?[y/n]")).lower()
                if(ans=='y'):
                    guest_list.append(n)
                    print(f"{n} is Successfully added to guest_list")
                else:
                    print("OK, as you wish")
        case 6:
            print("names are:")
            for i,v in enumerate(guest_list):
                print(f"{i+1}\t{v}")
            i=int(input("Enter index of value to update: "))-1
            if x < len(guest_list):
                up=input("Enter value to update: ")
                guest_list.pop(i)
                guest_list.insert(i,up)
            print("Successfully updated")
            else:
                print("Invalid index given")
        case 7:
            print(f"No.of guests are {len(guest_list)}")
        case 8:
            print("Thank you for using our application!")
            break
        case _:print("Invalid input, Try again")
    print()
            
