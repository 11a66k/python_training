from model.contact import Contact
from  random import randrange



def test_modif_first_name(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(last_name="test",
                                       email="123@32.32", email2="123", email3="2"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(first_name="Pinkey", last_name="test",
                      email="123@32.32", email2="123", email3="2")
    contact.id = old_contact[index].id
    app.contact.modif_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == app.contact.count()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modif_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(last_name="test"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.modif_first_first_name(Contact(last_name="Pye"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)