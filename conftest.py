import pytest
from fixture.application import Applicaion


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Applicaion()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Applicaion()
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture