class WeatherData:
    def __init__(self) -> None:
        pass

    def raise_exception_data(self) -> dict:
        return {
            "max": 40.3,
            "min": 40.6,
            "feels like": 37.29,
            "wind": 10.3570322,
            "rain": None,
            "snow": {},
        }

    def default_data(self) -> dict:
        return {
            "max": 40.3,
            "min": 40.6,
            "feels like": 37.29,
            "wind": 10.3570322,
            "rain": {},
            "snow": {},
        }
