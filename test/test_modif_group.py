
from model.group import Group


def test_modif_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group()
    app.group.fiil_form(Group(name="aaa", header="sss", footer="ddd"))
    app.group.sumbit_modif()
    app.session.logout()
