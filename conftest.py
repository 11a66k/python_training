import pytest
from fixture.application import Applicaion


@pytest.fixture(scope = "session")
def app(request):
    fixture = Applicaion()
    request.addfinalizer(fixture.destroy)
    return fixture