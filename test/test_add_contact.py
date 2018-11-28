# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact



def test_add_contact(app, json_contacts, db, chech_ui):
    contact = json_contacts
    old_contact = db.get_contact_list()
    app.contact.create_new(contact)
    new_contact = db.get_contact_list()
    # assert len(old_contact) + 1 == app.contact.count()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if chech_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




