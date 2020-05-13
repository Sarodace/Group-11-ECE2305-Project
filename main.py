# LIBRARIES
from twilio.rest import Client # Twilio library
import os # Used for Environment Variables
from gpiozero import Button # Used for our switch
# import keyboard # Used for testing code w/o RPi
from time import sleep # So our code isn't continously checking
from datetime import datetime as dt # For timestamps
from datetime import time

# FUNCTIONS
def suffix(d):
  return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
  return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def is_current_time_between(begin_time, end_time):
    check_time = dt.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time

# VARIABLES
button = Button(24) # Switch connected to GPIO 24
buttonPressed = 0

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

# "MAIN"
while True:
  if button.is_pressed and buttonPressed == 0:
    if is_current_time_between(time(8,55), time(10,5)):
      message = client.messages.create(
          to=os.environ['RECIPIENT_PHONE_NUMBER'],
          from_=os.environ['SENDER_PHONE_NUMBER'],
          body=custom_strftime("You've got mail! A package was delivered on %B {S}, %Y at %H:%M:%S.", dt.now()))
      print("Mailbox door opened for first time by mailperson")
      print(message.sid)
    else:
      print("Mailbox door opened by homeowner")
    buttonPressed = 1
  if button.is_pressed and buttonPressed == 1:
    print("Mailbox currently open and awaiting closure")
  if not button.is_pressed:
    print("Mailbox closed")
    buttonPressed = 0
  sleep(1)