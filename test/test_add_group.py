# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.init_creation()
    app.group.fiil_form(Group(name="222", header="1111", footer="2222"))
    app.group.sumbit_creation()
    app.open_home_page()


def test_add_empty_group(app):
    app.group.init_creation()
    app.group.fiil_form(Group(name="", header="", footer=""))
    app.group.sumbit_creation()



if __name__ == "__main__":
    unittest.main()
