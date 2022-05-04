from app.db import IncomingNumbers
from app.crud import User
from app.conftest import added_user, first_time_user, msg
from datetime import datetime as dt

user = User()
# def test_add_number(added_user):

#     number, created_at = added_user
#     user.add_number(number, created_at)
#     assert IncomingNumbers.query.filter_by(number=number) is not None


# def test_add_number():
#     user = User()
#     here = user.add_number("1234", dt.today().date())
#     assert here is not None


def test_get_city(msg):
    valid_msg, invalid_msg = msg
    assert user.get_city(valid_msg) == "Knoxville"
    assert user.get_city(invalid_msg) is None


# def test_get_coords(msg):
#     valid_msg, invalid_msg = msg
#     assert user.get_coords(valid_msg) == [35.9603948, -83.9210261]
#     assert user.get_coords(invalid_msg) is None


# def test_is_body_valid(msg):
#     valid_msg, invalid_msg = msg
#     assert user.is_body_valid(valid_msg) is True
#     assert user.is_body_valid(invalid_msg) is False


# def test_is_first_time_user(first_time_user):
#     assert user.is_first_time_user(first_time_user[0]) is True


# def test_is_first_time_user_edge_case(added_user):
#     assert user.is_first_time_user(added_user[0]) is False


# def test_is_daily_limit_reached(added_user):
#     assert user.is_daily_limit_reached(added_user[0]) is True


# def test_is_daily_limit_reached_edge_case(first_time_user):
#     assert user.is_daily_limit_reached(first_time_user[0]) is False
