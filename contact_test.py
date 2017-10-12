import unittest  # Importing the uniitest module
import pyperclip
from contact import Contact  # import the Contact class


class TestContact(unittest.TestCase):

    def setUp(self):

        self.new_contact = Contact(
            "Peter", "Maina", "072012131", "petersoleeh@yahoo.com")  # create contact object

    def test_init(self):
        self.assertEqual(self.new_contact.first_name, "Peter")
        self.assertEqual(self.new_contact.last_name, "Maina")
        self.assertEqual(self.new_contact.phone_number, "072012131")
        self.assertEqual(self.new_contact.email, "petersoleeh@yahoo.com")

    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def tearDown(self):
        Contact.contact_list = []

    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")  # new contact_list
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                                       "test@user.com")  # new contact_list
        test_contact.save_contact()

        self.new_contact.delete_contact()  # delete contact
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        # test to check if we can find a contact by phone number
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                                               "test@user.com")  # new contact_list
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0712345678")

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")  # new contact_list
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0712345678")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):

        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):

        # test to confirm we are copying the email address from a found contact
        self.new_contact.save_contact()
        Contact.copy_email("072012131")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
