from model.contact import Contact
from  random import randrange
import random



def test_modify_contact_name(app, db, chech_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(last_name="123213", first_name="123"))
    old_contact = db.get_contact_list()
    random_contact = random.choice(old_contact)
    contact = Contact(last_name="123", first_name="123")
    contact.id = random_contact.id
    app.contact.modif_contact_by_id(random_contact.id, contact)
    new_contact = db.get_contact_list()
    old_contact.remove(random_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if chech_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.id_or_max)

