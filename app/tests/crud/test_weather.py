import pytest
from dataclasses import asdict

from app.crud import Weather
from app.tests.data import user_1, user_2, user_3


def test_check_weather_data():
    weather = Weather()
    assert weather.check_weather_data(user_1()) is True
    assert weather.check_weather_data(user_2()) is False


def test_coerce_floats():
    weather = Weather()
    with pytest.raises(Exception):
        weather.coerce_floats(asdict(user_3()))
