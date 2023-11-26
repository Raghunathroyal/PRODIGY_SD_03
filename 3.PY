import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def edit_contact(contacts):
    view_contacts(contacts)

    try:
        index_to_edit = int(input("Enter the index of the contact you want to edit: ")) - 1
        if 0 <= index_to_edit < len(contacts):
            contact_to_edit = contacts[index_to_edit]
            print("Editing contact:")
            print(f"1. Name: {contact_to_edit['Name']}")
            print(f"2. Phone: {contact_to_edit['Phone']}")
            print(f"3. Email: {contact_to_edit['Email']}")

            field_to_edit = int(input("Enter the number of the field you want to edit: "))
            if 1 <= field_to_edit <= 3:
                new_value = input(f"Enter the new value for {['Name', 'Phone', 'Email'][field_to_edit - 1]}: ")
                contact_to_edit[list(contact_to_edit.keys())[field_to_edit - 1]] = new_value
                print("Contact edited successfully!")
            else:
                print("Invalid field number.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)

    try:
        index_to_delete = int(input("Enter the index of the contact you want to delete: ")) - 1
        if 0 <= index_to_delete < len(contacts):
            contact_deleted = contacts.pop(index_to_delete)
            print(f"Contact {contact_deleted['Name']} deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
