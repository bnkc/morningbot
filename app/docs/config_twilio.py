import os
from dotenv import load_dotenv

from twilio.rest import Client

load_dotenv()


class Twilio:
    """Twilio API"""

    SENDERS = os.getenv("SENDERS")
    TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    NOTIFY_SERVICE_SID = os.getenv("TWILIO_NOTIFY_SERVICE_SID")
    CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
