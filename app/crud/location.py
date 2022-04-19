from typing import List, Tuple

import geocoder
from geotext import GeoText


def city_and_coord(message: str) -> Tuple[str, List[float]]:
    """
    Returns the city and coordinates of the message.

    :param message: Inbound message.
    """
    try:
        city = GeoText(message).cities[0]
        coordinates = geocoder.osm(message).latlng
        return city, coordinates
    except IndexError:
        raise ValueError(f"Error: {message} is not a city")
