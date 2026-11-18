def show_admin_menu(): 
    print("==Admin Menu:")    
    print("     1. Accommodations, floors, rooms & facilities")
    print("     2. Residents & tenancies")
    print("     3. Cleaning rotas")
    print("     4. Fridge slots")
    print("     5. Repairs")
    print("     6. Dashboard")
    print("     0. Log out")

    choice = input("Please select an option: ")
    return choice

def show_admin_residents_menu():
    print("==Admin Residents Menu:")
    print("     1. Residents")
    print("     2. Tenancies")
    print("     0. Back to Admin Menu")

    choice = input("Please select an option: ")
    return choice


def run_admin():
    while True:
        choice = show_admin_menu()
        if choice == "1":
            print("Accommodations, floors, rooms & facilities selected.")
            # Add logic for this option
        elif choice == "2":
            print("Residents & tenancies selected.")
            # Add logic for this option  
        elif choice == "3":
            print("Cleaning rotas selected.")
            # Add logic for this option
        elif choice == "4":
            print("Fridge slots selected.")
            # Add logic for this option
        elif choice == "5":
            print("Repairs selected.")
            # Add logic for this option
        elif choice == "6":
            print("Dashboard selected.")
            # Add logic for this option
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def run_residents():
    while True:
        choice = show_admin_residents_menu()
        if choice == "1":
            print("Residents selected.")
            # Add logic for this option
        elif choice == "2":
            print("Tenancies selected.")
            # Add logic for this option  
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")