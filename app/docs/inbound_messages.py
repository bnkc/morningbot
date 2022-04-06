import os
from typing import Any, List

from geotext import GeoText

from .config_twilio import Twilio


def inbound_location(messages: List[Any]) -> str:
    """
    This function takes in a list of messages and returns the location of the
    first message that contains a location.

    :param messages: A list of messages.

    :return: The location of the inbound message.
    if no location is found, default to location.
    """

    twilio_number = Twilio.TWILIO_NUMBER
    last_message = max(messages, key=lambda x: x == twilio_number)
    inbound_city = GeoText(last_message.body).cities[0]
    if inbound_city is None:
        inbound_city = os.environ["DEFAULT_LOCATION"]
    return inbound_city
