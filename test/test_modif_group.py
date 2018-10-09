
from model.group import Group


def test_modif_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group(Group(name="neeee"))
    app.session.logout()


def test_modif_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group(Group(header="sss"))
    app.session.logout()
