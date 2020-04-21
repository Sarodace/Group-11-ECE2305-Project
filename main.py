# Twilio library
from twilio.rest import Client

# Used for Environment Variables
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.environ['RECIPIENT_PHONE_NUMBER'],
    from_=os.environ['SENDER_PHONE_NUMBER'],
    body="Hello, World!")

print(message.sid)