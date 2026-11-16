def show_menu():
    print("Welcome to the CLI Menu!")
    print("1. Tenant")
    print("2. Maintenance Requests")
    print("3. Exit")

    choice = input("Please select an option: ")
    return choice   

def run():
    while True:
        choice = show_menu()
        if choice == "1":
            print("Tenant selected.")
            # Add logic for Tenant
        elif choice == "2":
            print("Maintenance Requests selected.")
            # Add logic for Maintenance Requests
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()