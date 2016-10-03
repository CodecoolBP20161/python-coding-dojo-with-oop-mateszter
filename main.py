class ContactList(list):
    def search(self, input_contact):
        contact_list = [i for i in self if input_contact in i.name]
        #contact_list = filter(lambda x: x. == value, self)

        return contact_list

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append([self])

    @classmethod
    def reset_contacts(cls):
        return cls.all_contacts.clear()


class Supplier(Contact):
    all_orders = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def order(self, string):
        try:
            Supplier.all_orders[self.email].append(string)
        except:
            Supplier.all_orders[self.email] = [string]
