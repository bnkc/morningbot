import pytest

from app.schemas import TestData
from app.crud import Message


def test_temp_rules_raises_exception():
    test = TestData()
    with pytest.raises(Exception):
        Message.temp_set_rules(Message(test.default_data()))


def test_rain_rules_raises_exception():
    test = TestData()
    with pytest.raises(Exception):
        Message.rain_set_rules(Message(test.default_data()))


def test_snow_rules_raises_exception():
    test = TestData()
    with pytest.raises(Exception):
        Message.snow_set_rules(Message(test.default_data()))


def test_wind_rules_raises_exception():
    test = TestData()
    with pytest.raises(Exception):
        Message.wind_set_rules(Message(test.default_data()))
