class DemoUser:
    def __init__(self) -> None:
        pass

    def user_1(self) -> dict:
        return {
            "max temp": 40.3,
            "min temp": 40.6,
            "feels like": 45.29,
            "wind speed": None,
            "detailed status": "Clear sky",
            "uv index": 4,
            "location": "London, GB",
        }

    def user_2(self) -> dict:
        return {
            "max temp": 40.3,
            "min temp": 40.6,
            "feels like": 45.29,
            "wind speed": 34.5,
            "detailed status": "Clear sky",
            "uv index": 4,
            "location": "London, GB",
        }
