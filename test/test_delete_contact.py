from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count == 0:
        app.contact.create_new(Contact(last_name="test"))
    app.contact.delete_first()

