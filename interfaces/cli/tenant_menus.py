def show_tenant_menu():
    print("==Tenant Menu:")
    print("     1. My details")
    print("     2. My cleaning duties")
    print("     3. My fridge slot")
    print("     4. Report a repair")
    print("     5. My repairs")
    print("     0. Log out")
    choice = input("Please select an option: ")
    return choice

def run_tenant():
    while True:
        choice = show_tenant_menu()
        if choice == "1":
            print("My details selected.")
            # Add logic for this option
        elif choice == "2":
            print("My cleaning duties selected.")
            # Add logic for this option
        elif choice == "3":
            print("My fridge slot selected.")
            # Add logic for this option
        elif choice == "4":
            print("Report a repair selected.")
            # Add logic for this option
        elif choice == "5":
            print("My repairs selected.")
            # Add logic for this option
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")