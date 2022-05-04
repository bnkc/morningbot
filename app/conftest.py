from datetime import datetime as dt
import pytest
import random


@pytest.fixture
def added_user():
    number = "+1234"
    created_at = dt.today().date()
    return number


@pytest.fixture
def first_time_user():
    number = str(random.randint(1, 1000))
    created_at = dt.today().date()
    return number, created_at


@pytest.fixture
def msg():
    valid_msg = "Knoxville TN United States"
    invalid_msg = "This is not a city"
    return valid_msg, invalid_msg
