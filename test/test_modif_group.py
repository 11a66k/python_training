
from model.group import Group


def test_modif_group_name(app):
    app.group.modif_first_group(Group(name="neeee"))


def test_modif_group_header(app):
    app.group.modif_first_group(Group(header="sss"))
