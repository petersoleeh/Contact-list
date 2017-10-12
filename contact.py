import pyperclip


class Contact:
    """docstring for Contact."""

    contact_list = []

    def __init__(self, first_name, last_name, phone_number, email):

        self.first_name = first_name  # these are class properties
        self.last_name = last_name  # these are class properties
        self.phone_number = phone_number  # these are class properties
        self.email = email  # these are class properties

    def save_contact(self):
        '''
        save contacts
        '''

        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete a saved contact
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True

        return False

    @classmethod
    def display_contacts(cls):  # return the contact list
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
# super(Contact, self).__init__()
    # self.arg = arg
