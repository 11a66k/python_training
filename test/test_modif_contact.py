from model.contact import Contact


def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modif_first_first_name(Contact(first_name="Pinkey"))
    app.session.logout()

def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modif_first_first_name(Contact(last_name="Pye"))
    app.session.logout()


def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modif_first_first_name(Contact(first_name="Pinkey", last_name="Pye", address="RUSSIA", phone_home="+11212", email="sa3@sa.sa"))
    app.session.logout()

