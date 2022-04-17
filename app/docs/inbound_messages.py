import os
from geopy.geocoders import Photon
import geocoder

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

    # incoming_numbers = set(
    #     [message.from_ for message in messages if message.from_ != twilio_number]
    # )
    # user_messages: list = []
    # for number in incoming_numbers:
    #     last_message = max(messages, key=lambda x: x.from_ == number)
    #     location = GeoText(last_message.body)
    #     if location.cities:
    #         user = {"number": number, "location": location.cities[0]}
    #         user_messages.append(user)
    # last_messages["number"] = number
    # last_messages["location"] = location.cities[0]
    # return user_messages
    # last_message = max(messages, key=lambda x: x.to == twilio_number)
    # number = last_message.from_
    inbound_city = GeoText(messages).cities[0]
    if inbound_city is None:
        inbound_city = os.environ["DEFAULT_LOCATION"]
    return inbound_city


def coordinates(messages) -> str:
    """
    This function takes in a list of messages and returns the coordinates

    :param messages: A list of messages.

    :return: The coordinates of the location.
    """

    # twilio_number = Twilio.TWILIO_NUMBER
    # last_message = max(messages, key=lambda x: x.to == twilio_number)
    coordinates = geocoder.osm(messages)
    if coordinates is None:
        coordinates = os.environ["DEFAULT_COORDINATES"]
    return coordinates.latlng


# print(inbound_location(Twilio.CLIENT.messages.list()))
# print(coordinates(Twilio.CLIENT.messages.list()))
