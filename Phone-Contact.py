contacts = {}

while True:
    print("\nOptions:")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for a contact by name")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added to contacts.")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        break

    else:
        print("invalid")
