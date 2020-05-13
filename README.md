# Project Title

This repository contains the code for Team 11's course project for ECE2305 - Introduction to Communications and Networks. (Elaborate on this until we have a paragraph describing the content of the course, what we chose as our course project, and what specific material we chose to implement. 

## Getting Started

(This'll eventually describe how people can get this software installed on their personal devices)

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Quick start 

1. Clone repository to desktop by running  ``` git clone [web URL] ``` where the ```[web URL]``` is gotten from the "Clone or download" button.

NEED TO TALK ABOUT PIP INSTALL

2. Add TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, RECIPIENT_PHONE_NUMBER, and SENDER_PHONE_NUMBER environment variable declarations to the startup file. This can be done through opening that file with ```sudo nano /etc/rc.local```. Once nano has opened at that file, you'll add ``` export [ENVIRONMENT_VARIABLE]=[RELEVANT_INFORMATION] ``` before the line which says "exit 0". You'll add this four times and every line's [ENVIRONMENT_VARIABLE] will be substituted with one of the four variables that needs to be declared. The [RELEVANT_INFORMATION] will only be provided to members of Team 11 and, by request, to the intructor and TAs of ECE2305.

NOTE: You cannot progress past this step if you don't fall within one of those two extremely narrow groups. Despite that, feel free to utilize the code for your own pursuits!

3. Add ``` Lxterminal -e python “/home/Desktop/Group-11-ECE2305-Project/main.py” ``` to that same file. This ensures that the program always runs on startup.

NOTE: This command assumes that the python file is located in the "./Group-11-ECE2305-Project" folder on the desktop


End with an example of getting some data out of the system or using it for a little demo

## Deployment

TALK ABOUT HOW EVERYTHING IS WIRED TOGETHER

## Built With

* [Twilio](https://www.twilio.com/) - Used to send SMS messages
* [RESOURCE NAME](http://www.google.com) - BLURB
* [RESOURCE NAME](http://www.google.com) - BLURB

## Authors

* **Samantha Boyea** - *DESCRIBE CONTRIBUTIONS* - [sboyea](https://github.com/sboyea)
* **Emily Bubencik** - *DESCRIBE CONTRIBUTIONS* - [emilyb53](https://github.com/emilyb53)
* **Ryan Devendorf** - *DESCRIBE CONTRIBUTIONS* - [ryanDevendorf](https://github.com/ryanDevendorf)
* **Jonathan Ferreira** - *DESCRIBE CONTRIBUTIONS* - [Sarodace](https://github.com/Sarodace)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* USE THIS TO THANK PEOPLE WHOSE CODE WE USED
* INSPIRATION
* etc
