import os
from twilio.rest import Client
from dotenv import load_dotenv

from app.crud import Message


load_dotenv()

sender = os.getenv("SENDER")
twilio_number = os.getenv("TWILIO_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=Message.from_current().create_message(),
    from_=twilio_number,
    to=sender,
)

print(message.sid)


# import sys

# print(sys.path[0])
