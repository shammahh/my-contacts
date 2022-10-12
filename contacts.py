

from operator import index, indexOf



def contains(arr, item):
    for element in arr:
        if element == item:
            return True
    
    return False

contacts = []

james = ["james", 333, "james.email"]
shelly = ["shelly", 444, "shelly.email"]
contacts.append(james)
contacts.append(shelly)
print(contacts)

loop = True
while loop:    ### menu
    print("\nMAIN MENU")
    print("1 - Display Contact Names")
    print("2 - Search for Contact")
    print("3 - Edit Contact")
    print("4 - New Contact")
    print("5 - Remove Contact")
    print("6 - Exit")
    ### menu selection
    runfun = int(input("Enter selection 1-6:  "))
    if runfun == 1:
        print("\nDISPLAY CONTACT NAMES")
        print(f"Contact 1: {contacts[0][0]} ({contacts[0][1]})")
        print(f"Contact 2: {contacts[1][0]} ({contacts[1][1]})")
        ### use json DATA --->> STRING
    elif runfun == 2:
        print("Option 2")
        xez = input("Search contact by name  ")
        for i in range(len(contacts)):
            if contains(contacts[i], xez) == True:
                print(contacts[i])
    elif runfun == 3:
        print("Option 3")
        opchoice = input("Which contacts would you like to edit  ")
        newname = input("input new name  ")
        newnum = input("input new number  ")
        newmail = input("input new email  ")
        for i in range(len(contacts)):
            if contains(contacts[i], opchoice) == True:
                contacts[i] = [newname, newnum, newmail]
                print(contacts[i])
    elif runfun == 4:
        print("Option 4")
        contactname = input("What would you like to call this contact  ")
        newA = input("Contact name  ")
        newB = input("Contact number  ")
        newC = input("Contact Email  ")
        contactname = [newA, newB, newC]
        contacts.append(contactname)
    elif runfun == 5:
        print("Option 5")
        print(contacts)
        removechoice = input("Which contact to remove (contact name)  ")
        for i in range(len(contacts)):
            if contains(contacts[i], removechoice) == True:
                contacts.pop(i)
        print(contacts)
    elif runfun == 6:
        loop = False
