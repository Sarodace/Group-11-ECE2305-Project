# IOT Mail Delivery Notification System

This repository contains the code for Team 11's course project for ECE2305 - Introduction to Communications and Networks. In this course, we extenively covered the five layer TCP/IP model and various other networking models. A large focus of the course was to work in teams to design and build a custom Internet-of-Things prototype. Our team came up with a Raspberry Pi-based solution to knowing when one's mail has arrived. The mailbox sends an SMS message to the user when their mail has been delivered to their house. The idea behind the prototype is so people using the design will automatically know when their mail has arrived, so they won't have to impulsively check their mailbox.


## Getting Started

This project relies on a stable internet connection, so, in order to proceed, it's advised that you make sure that your Raspberry Pi is connected to the internet.


### Prerequisites

#### Hardware

* (1) Raspberry Pi 3 model B micro-controller (MCU)
* (1) Breadboard
* (1) RAVPower Deluxe Series Portable Charger
* (1) Contact switch

#### Software

Since this project depends on the Twilio library, it's required for it to be installed to your Raspberry Pi. This can be done by running the following command:

```
pip2.7 install Twilio
```


### Quick start 

1. Clone repository to desktop by running  ``` git clone [web URL] ``` where the ```[web URL]``` is gotten from the "Clone or download" button.


2. Add TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, RECIPIENT_PHONE_NUMBER, and SENDER_PHONE_NUMBER environment variable declarations to the startup file. This can be done through opening that file with ```sudo nano /etc/rc.local```. Once nano has opened at that file, you'll add ``` export [ENVIRONMENT_VARIABLE]=[RELEVANT_INFORMATION] ``` before the line which says "exit 0". You'll add this four times and every line's [ENVIRONMENT_VARIABLE] will be substituted with one of the four variables that needs to be declared. The [RELEVANT_INFORMATION] will only be provided to members of Team 11 and, by request, to the intructor and TAs of ECE2305.

    NOTE: You cannot progress past this step if you don't fall within one of those two extremely narrow groups. Despite that, feel free to utilize the code for your own pursuits!

    

3. Add ``` Lxterminal -e python “/home/Desktop/Group-11-ECE2305-Project/main.py” ``` to that same file. This ensures that the program always runs on startup.

    NOTE: This command assumes that the python file is located in the "./Group-11-ECE2305-Project" folder on the desktop

4. Reboot your Raspberry Pi and watch it run!


## Built With

* [Twilio](https://www.twilio.com/) - Used to send SMS messages
* [gpiozero](https://gpiozero.readthedocs.io/en/stable/) - Used to interface with RPi GPIO


## Authors

* **Samantha Boyea** - *Assembling the mailbox & implementation* - [sboyea](https://github.com/sboyea)
* **Emily Bubencik** - *Assist where needed* - [emilyb53](https://github.com/emilyb53)
* **Ryan Devendorf** - *Programming the Raspberry Pi* - [ryanDevendorf](https://github.com/ryanDevendorf)
* **Jonathan Ferreira** - *Programming the Raspberry Pi* - [Sarodace](https://github.com/Sarodace)

All authors met extensively throughout the term to test the functionality of the project. 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details