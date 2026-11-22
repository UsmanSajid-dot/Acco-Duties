from interfaces.cli.admin_menus import run_admin
from interfaces.cli.tenant_menus import run_tenant

def show_menu():
    print("====Welcome to Acco Duties!===")
    print("===Your accomodation problems solved with a click!")
    print("==Are you the Tenant or the Admin?")
    print("==Please select an option:")
    print("     1. Tenant")
    print("     2. Admin")
    print("     0. Exit")

    choice = input("Please select an option: ")
    return choice  

def run(services):
    while True:
        choice = show_menu()
        if choice == "1":
            print("Tenant selected.")
            # Add logic for Tenant
            run_tenant(service)
        elif choice == "2":
            print("Admin selected.")
            # Add logic for Admin
            run_admin(services)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
