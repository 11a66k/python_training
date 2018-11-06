# -*- coding: utf-8 -*-

from model.contact import Contact



def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(first_name="rick", last_name="mortiy", address="USA", phone_home="a", phone_mobile="b", phone_work="c", email="123@32.32")
    app.contact.create_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)



