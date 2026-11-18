def show_menu():
    print("Welcome to the CLI Menu!")
    print("Are you the Tenant or the Admin?")
    print("Please select an option:")
    print("1. Tenant")
    print("2. Admin")
    print("3. Exit")

    choice = input("Please select an option: ")
    return choice  

def show_admin_menu(): 
    print("Admin Menu:")    
    print("1. Accommodations, floors, rooms & facilities")
    print("2. Residents & tenancies")
    print("3. Cleaning rotas")
    print("4. Fridge slots")
    print("5. Repairs")
    print("6. Dashboard")
    print("0. Log out")

    choice = input("Please select an option: ")
    return choice

def show_tenant_menu():
    print("Tenant Menu:")
    print("1. My details")
    print("2. My cleaning duties")
    print("3. My fridge slot")
    print("4. Report a repair")
    print("5. My repairs")
    print("0. Log out")
    choice = input("Please select an option: ")
    return choice

def run():
    while True:
        choice = show_menu()
        if choice == "1":
            print("Tenant selected.")
            # Add logic for Tenant
            choice = show_tenant_menu()
        elif choice == "2":
            print("Admin selected.")
            choice = show_admin_menu()

            # Add logic for Admin
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()