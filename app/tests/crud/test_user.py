from app.crud import CheckUser


def test_is_body_valid():

    assert CheckUser.is_body_valid("this is not a city") is False


def test_is_first_time_user():

    assert CheckUser.is_first_time_user("123456789") is True


def test_is_daily_limit_reached():

    assert CheckUser.is_daily_limit_reached("123456789") is False
