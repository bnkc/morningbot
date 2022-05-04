from typing import List, Tuple, Optional

import geocoder
from geotext import GeoText


def city_and_coord(message: str) -> Optional[Tuple[str, List[float]]]:
    """
    Returns the city and coordinates of the message.
    """
    try:
        city = GeoText(message).cities[0]
        coordinates = geocoder.osm(message).latlng
        return city, coordinates
    except IndexError:
        return None


# heeyyyyyy this is peter
