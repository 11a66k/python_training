from model.contact import Contact


def test_modif_first_name(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(last_name="test"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(first_name="Pinkey", last_name="test")
    contact.id = old_contact[0].id
    app.contact.modif_first_first_name(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == app.contact.count()
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modif_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(last_name="test"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.modif_first_first_name(Contact(last_name="Pye"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)