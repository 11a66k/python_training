# -*- coding: utf-8 -*-

from model.contact import Contact



def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create_new(Contact(first_name="rick", last_name="mortiy", address="USA", phone_home="+1000000", email="123@32.32"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)



