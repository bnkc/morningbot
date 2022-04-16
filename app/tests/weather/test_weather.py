# import pytest

# from app.weather import CurrentWeather
# from app.schemas import TestData
# from app.crud import format_data


# def test_current():
#     assert isinstance(format_data()["max"], int)
#     assert isinstance(format_data()["min"], int)
#     assert isinstance(format_data()["feels like"], int)
#     assert isinstance(format_data()["wind"], int)
#     assert isinstance(format_data()["location"], str)
#     assert isinstance(format_data()["detailed_status"], str)


# def test_current_raises_exception():
#     weather = CurrentWeather()
#     with pytest.raises(Exception):
#         weather.current(TestData.raise_exception_data)
