class TestData:
    def __init__(self) -> None:
        pass

    def raise_exception_data(self) -> dict:
        return {
            "max": 40.3,
            "min": 40.6,
            "feels like": 72.29,
            "wind": 10.3570322,
            "rain": None,
            "snow": {},
        }

    def default_data(self) -> dict:
        return {
            "max": 40.3,
            "min": 40.6,
            "feels like": 370.29,
            "wind": -10.3570322,
            "rain": -4.0,
            "snow": -4.0,
            "location": "London, GB",
            "detailed_status": "Clear sky",
        }


# if __name__ == "__main__":
#     test = TestData()
#     print(test.default_data())
