from app.crud import Message
from app.docs import Twilio


def send_bulk_sms() -> None:
    """
    Send a bulk SMS to all users.
    """
    numbers = Twilio.SENDERS.split(",")

    for number in numbers:
        Twilio.CLIENT.messages.create(
            body=Message.from_current().create_message(),
            from_=Twilio.TWILIO_NUMBER,
            to=number,
        )


send_bulk_sms()
