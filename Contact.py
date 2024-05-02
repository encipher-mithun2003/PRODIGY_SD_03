import json

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def edit_contact(self, index, name, phone_number, email):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(**contact) for contact in data]
        except FileNotFoundError:
            print("Contact file not found.")

def main():
    contact_manager = ContactManager()
    contact_manager.load_contacts_from_file("contacts.json")  # Load contacts from file if it exists

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(Contact(name, phone_number, email))
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter updated name: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            contact_manager.edit_contact(index, name, phone_number, email)
        elif choice == '4':
            index = int(input("Enter index of contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '5':
            contact_manager.save_contacts_to_file("contacts.json")
            print("Contacts saved to file.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
