import os
from dotenv import load_dotenv

from twilio.rest import Client

load_dotenv()


class Twilio:
    """Twilio API"""

    SENDERS = os.environ["SENDERS"]
    TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
    ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
    AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
    NOTIFY_SERVICE_SID = os.environ["TWILIO_NOTIFY_SERVICE_SID"]
    CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
