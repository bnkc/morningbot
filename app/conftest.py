from datetime import datetime as dt
import pytest
import random


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
    msg = "Knoxville TN United States"
    return msg

@pytest.fixture
def invalid_msg():
    msg = "This is not a city"
    return msg