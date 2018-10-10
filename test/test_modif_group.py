
from model.group import Group


def test_modif_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modif_first_group(Group(name="neeee"))


def test_modif_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modif_first_group(Group(header="sss"))
