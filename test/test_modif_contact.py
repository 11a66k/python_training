from model.contact import Contact



def test_modif_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modif_first()
    app.contact.fill_form(Contact(first_name="Pinkey", last_name="Pye", address="RUSSIA", phone_home="+11212", email="sa3@sa.sa"))
    app.contact.update_form()
    app.session.logout()