import os

from .inbound_messages import inbound_location
from .config_twilio import Twilio


class WeatherApi:
    """Weather API"""

    WX_API_KEY = os.getenv("WX_API_KEY")
    WX_LOCATION = inbound_location(Twilio.CLIENT.messages.list())
    WX_METRIC_TEMP = os.environ.get("WX_METRIC_TEMP", "fahrenheit")
    WX_METRIC_WIND = os.environ.get("WX_METRIC_WIND", "miles_hour")
