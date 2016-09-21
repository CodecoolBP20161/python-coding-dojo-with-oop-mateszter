
class Contact:
    all_contacts = []

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

    @classmethod
    def order(cls, string):
        pass
