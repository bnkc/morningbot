# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
from crud import Message

load_dotenv()

sender = os.getenv("SENDER")
twilio_number = os.getenv("TWILIO_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=Message().create_message(),
    from_=twilio_number,
    to=sender,
)

print(message.sid)
