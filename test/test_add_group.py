# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Applicaion




@pytest.fixture
def app(request):
    fixture = Applicaion()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.init_group_creation()
    app.fiil_group_form(Group(name="222", header="1111", footer="2222"))
    app.sumbit_group_creation()
    app.session.logout()


def test_case_add_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.init_group_creation()
    app.fiil_group_form( Group(name="", header="", footer=""))
    app.session.logout()



if __name__ == "__main__":
    unittest.main()
