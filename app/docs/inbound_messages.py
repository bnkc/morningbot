import os
from geotext import GeoText

from .config_twilio import Twilio


def inbound_location() -> str:
    """
    Return the location of the inbound message.

    loop through the inbound messages and return the location.
    If the location is not found, return set default location.
    """

    default_location = os.getenv("DEFAULT_LOCATION")
    twilio_number = Twilio.TWILIO_NUMBER

    try:
        for key, sms in enumerate(Twilio.CLIENT.messages.list()):
            if key == 0 and sms.to == twilio_number:
                inbound_city = GeoText(sms.body).cities[0]
                break
            else:
                inbound_city = default_location
                break
    except IndexError:
        raise IndexError("No inbound location found in last message to Twilio.")
    return inbound_city


print(inbound_location())
