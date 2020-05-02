from gpiozero import Button
from time import sleep

# Button connected to GPIO 24
button = Button(24)

while True:
  if button.is_pressed:
    print("Mailbox open")
  else:
    print("Mailbox closed")
  sleep(1)
