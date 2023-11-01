class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact.name, contact.phone)

    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_list = ContactList()

    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_list.add_contact(contact)
        elif choice == "2":
            contact_list.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term: ")
            results = contact_list.search_contacts(search_term)
            for contact in results:
                print(contact.name, contact.phone)
        elif choice == "4":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            old_contact = None
            for contact in contact_list.contacts:
                if contact.name == name and contact.phone == phone:
                    old_contact = contact
                    break
            if old_contact:
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                new_contact = Contact(new_name, new_phone, new_email, new_address)
                contact_list.update_contact(old_contact, new_contact)
        elif choice == "5":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contact = None
            for c in contact_list.contacts:
                if c.name == name and c.phone == phone:
                    contact = c
                    break
            if contact:
                contact_list.delete_contact(contact)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()