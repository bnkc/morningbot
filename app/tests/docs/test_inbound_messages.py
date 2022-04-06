import pytest
from app.docs import inbound_location


def test_inbound_location():
    with pytest.raises(Exception):
        inbound_location(None)
