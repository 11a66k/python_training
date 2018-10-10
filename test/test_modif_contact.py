from model.contact import Contact


def test_modif_first_name(app):
    if app.contact.count == 0:
        app.contact.create_new(Contact(last_name="test"))
    app.contact.modif_first_first_name(Contact(first_name="Pinkey"))


def test_modif_last_name(app):
    app.contact.modif_first_first_name(Contact(last_name="Pye"))


