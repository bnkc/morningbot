import os
from dotenv import load_dotenv


import googlemaps

load_dotenv()


class Config:
    """
    Class to store the configuration for crud weather app
    """

    manager = os.environ["WX_API_KEY"]
    metric_temp = os.environ.get("WX_METRIC_TEMP", "fahrenheit")
    metric_wind = os.environ.get("WX_METRIC_WIND", "miles_hour")
    gmaps = googlemaps.Client(key=os.environ["GEOLOCATION_API_KEY"])
