# -*- coding: utf-8 -*-

from model.contact import Contact



def test_add_contact(app):
    app.contact.create_new()
    app.contact.fill_form(Contact(first_name="rick", last_name="mortiy", address="USA", phone_home="+1000000", email="123@32.32"))
    app.contact.submin_form()



if __name__ == "__main__":
    unittest.main()
