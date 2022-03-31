from src import CurrentWeather
from helper import format_data


class Message:
    def __init__(self, weather):
        self.data = weather

    @classmethod
    def from_current(cls, weather_data=None):
        weather_data = format_data()
        return cls(weather_data)

    def temp_set_rules(self, temp=None) -> str:
        if self.data["feels like"] < 30:
            temp = "freezing"
        elif self.data["feels like"] > 30 and self.data["feels like"] < 45:
            temp = "pretty cold"
        elif self.data["feels like"] > 45 and self.data["feels like"] < 60:
            temp = "nippy"
        else:
            temp = "warm"
        return temp

    def rain_set_rules(self, rain=None) -> str:
        if self.data["rain"] > 0:
            rain = "will rain"
        else:
            rain = "not rain"
        return rain

    def wind_set_rules(self, wind=None) -> str:
        if self.data["wind"] > 5:
            wind = "windy"
        else:
            wind = "calm"
        return wind

    def create_message(self, message=None) -> str:
        message = f"Good morning! Today it will be {self.temp_set_rules()} feeling like {self.data['feels like']}°F. The High of the day is {self.data['max']}°F and the Low of the day is {self.data['min']}°F. It might be {self.wind_set_rules()} with wind speeds of {self.data['wind']}mph. Lastly, it will {self.rain_set_rules()} in {self.data['location']}."
        return message


# {'max': 43.21, 'min': 39.88, 'feels like': 35.17, 'wind': 11.4978716, 'rain': {}, 'snow': {}, 'location': 'Columbus US'}


message = Message.from_current()

print(message.create_message())
