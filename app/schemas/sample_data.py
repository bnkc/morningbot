class DemoUser:
    def __init__(self) -> None:
        pass

    def user_1(self) -> dict:
        return {
            "max": 40.3,
            "day": 40.6,
            "min": 40.6,
            "feels like": 45.29,
            "wind": None,
            "detailed_status": "Clear sky",
            "location": "London, GB",
        }

    def user_2(self) -> dict:
        return {
            "max": 40.3,
            "day": 40.6,
            "min": 40.6,
            "feels like": 45.29,
            "wind": 34.5,
            "detailed_status": "Clear sky",
            "location": "London, GB",
        }
