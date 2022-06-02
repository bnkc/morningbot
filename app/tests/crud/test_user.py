import pytest
from app.crud import User


user = User()


def test_get_area(valid_msg, invalid_msg):
    assert user.get_area(valid_msg) == "Erie County"
    with pytest.raises(ValueError):
        user.get_area(invalid_msg)


def test_get_coords(valid_msg, invalid_msg):
    assert user.get_coords(valid_msg) == [42.8982361, -78.6341996]
    with pytest.raises(ValueError):
        user.get_coords(invalid_msg)


def test_is_first_time_user(first_time_user):
    assert user.is_first_time_user(first_time_user[0])


def test_is_first_time_user_edge_case(added_user):
    assert user.is_first_time_user(added_user[0])


def test_is_daily_limit_reached(added_user):
    assert user.is_daily_limit_reached(added_user[0]) is False


def test_is_daily_limit_reached_edge_case(first_time_user):
    assert user.is_daily_limit_reached(first_time_user[0]) is False
