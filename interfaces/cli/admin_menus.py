from tracker.utils.exceptions import ValidationError
from tracker.utils.validators import is_valid_email

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


def run_admin(services):
    while True:
        choice = show_admin_menu()
        if choice == "1":
            print("Accommodations, floors, rooms & facilities selected.")
            # Add logic for this option
        elif choice == "2":
            print("Residents & tenancies selected.")
            # Add logic for this option  
            run_residents(services)
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

def run_residents(services):
    while True:
        choice = show_admin_residents_menu()
        if choice == "1":
            print("Residents selected.")
            # Add logic for this option
            run_residents_selected(services)
        elif choice == "2":
            print("Tenancies selected.")
            # Add logic for this option  
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def run_residents_selected(services):
    while True:
        choice = show_admin_residents_selected_menu()
        if choice == "1":
            print("Showing Residents")
            # Add logic for this option
            print(services.resident.list_residents())  # Example of calling a service method
        elif choice == "2":
            print("Adding a new Resident")
            # Add logic for this option
            name = input("Enter resident's name: ")
            email = input("Enter resident's email: ")
            phone = input("Enter resident's phone: ")
            try:
                is_valid_email(email)
                new_resident = services.resident.create_resident(name, email, phone)
                print(f"Resident added: {new_resident.name},\nEmail: {new_resident.email},\nPhone: {new_resident.phone},\nID: {new_resident.resident_id}")
            except ValidationError as e:
                print(f"Error: {e}")
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
    print("Press any key to return to the previous menu.")
    return

    # Add logic for this option

def run_residents_add(services):
    while True:
        choice = show_admin_residents_selected_menu()
        if choice == "1":
            print("Showing Residents")
            # Add logic for this option

        elif choice == "2":
            print("Adding a new Resident")
            # Add logic for this option
        elif choice == "3":
            print("Editing a Resident")
            # Add logic for this option
        elif choice == "4":
            print("Deleting a Resident")
            # Add logic for this option
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
    print("Press any key to return to the previous menu.")
    return