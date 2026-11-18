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
def show_admin_residents_selected_menu():
    print("==Admin Residents Selected Menu:")
    print("     1. Show Residents")
    print("     2. Add a new Resident")
    print("     3. Edit a Resident")
    print("     4. Delete a Resident")
    print("     0. Back to Admin Residents Menu")

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
            show_admin_residents_menu()
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
            run_residents_selected()
        elif choice == "2":
            print("Tenancies selected.")
            # Add logic for this option  
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def run_residents_selected():
    while True:
        choice = show_admin_residents_menu()
        if choice == "1":
            print("Showing Residents")
            # Add logic for this option
        elif choice == "2":
            print("Adding a new Resident")
            # Add logic for this option
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
    print("Press any key to return to the previous menu.")
    return

    # Add logic for this option