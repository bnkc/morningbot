import os
import json
from typing import List
from twilio.rest import Client

from dotenv import load_dotenv
from app.crud import Message

load_dotenv()

senders = os.getenv("SENDERS")
twilio_number = os.getenv("TWILIO_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
notify_service_sid = os.getenv("TWILIO_NOTIFY_SERVICE_SID")
client = Client(account_sid, auth_token)


def send_bulk_sms():
    for number in senders.split(","):
        client.messages.create(
            body=Message.from_current().create_message(),
            from_=twilio_number,
            to=number,
        )


send_bulk_sms()
