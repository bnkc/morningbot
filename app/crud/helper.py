from app.weather import CurrentWeather


def format_data() -> dict:
    """
    Format the data from the weather API
    """
    weather = CurrentWeather()
    data = weather.current(weather.get_weather_data)
    for key, val in data.items():
        if type(val) is float:
            data[key] = int(val)
    return data
