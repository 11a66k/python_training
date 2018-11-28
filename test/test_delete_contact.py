from model.contact import Contact
from  random import randrange
import random



def test_delete_contact(app, db,chech_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(last_name="test"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == app.contact.count()
    old_contact.remove(contact)
    assert old_contact == new_contact
    if chech_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# def test_delete_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(last_name="test"))
#     old_contact = app.contact.get_contact_list()
#     index = randrange(len(old_contact))
#     app.contact.delete_by_index(index)
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) - 1 == app.contact.count()
#     old_contact[index:index+1] = []
#     assert old_contact == new_contact

