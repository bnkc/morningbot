import pytest
from datetime import datetime as dt
import pytest
import random


from app.api import sms


@pytest.fixture()
def app():
    app = sms()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()


@pytest.fixture
def added_user():
    number = "+1234"
    created_at = dt.today().date()
    return number, created_at


@pytest.fixture
def first_time_user():
    number = str(random.randint(1, 1000))
    created_at = dt.today().date()
    return number, created_at


@pytest.fixture
def valid_msg():
    msg = "South Shady Street Lancaster, NY 14086"
    return msg


@pytest.fixture
def invalid_msg():
    msg = "This is not a city"
    return msg
