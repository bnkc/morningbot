import os
from typing import List
from geotext import GeoText

from .config_twilio import Twilio


def inbound_location(messages: List) -> str:
    """
    Return the location of an inbound message.

    loop through the inbound messages and return the city name.
    If the location is not found, return set default location.
    """

    default_location = os.getenv("DEFAULT_LOCATION")
    twilio_number = Twilio.TWILIO_NUMBER

    try:
        for key, sms in enumerate(messages):
            if sms.to == twilio_number:
                inbound_city = GeoText(sms.body).cities[0]
                break
            else:
                inbound_city = default_location

    except TypeError:
        raise TypeError("list was not iterable")
    return inbound_city
