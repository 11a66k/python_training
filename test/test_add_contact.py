# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Applicaion

@pytest.fixture
def app(request):
    fixture = Applicaion()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact()
    app.fill_contact_form(Contact(first_name="rick", last_name="mortiy", address="USA", phone_home="+1000000", email="123@32.32"))
    app.submin_form()
    app.session.logout()


if __name__ == "__main__":
    unittest.main()
