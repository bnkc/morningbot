from typing import List
from dotenv import load_dotenv

from app.crud import Message
from app.docs import Twilio


load_dotenv()


def send_bulk_sms() -> None:
    """Send a bulk SMS to all users."""
    for number in Twilio.SENDERS.split(","):
        Twilio.CLIENT.messages.create(
            body=Message.from_current().create_message(),
            from_=Twilio.TWILIO_NUMBER,
            to=number,
        )


send_bulk_sms()
