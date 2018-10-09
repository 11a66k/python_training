from model.contact import Contact


def test_modif_first_name(app):
    app.contact.modif_first_first_name(Contact(first_name="Pinkey"))

def test_modif_last_name(app):
    app.contact.modif_first_first_name(Contact(last_name="Pye"))


def test_modif_contact(app):
    app.contact.modif_first_first_name(Contact(first_name="Pinkey", last_name="Pye", address="RUSSIA", phone_home="+11212", email="sa3@sa.sa"))

