from twilio.rest import Client
from API_CODE import *
import smtplib
TWILIO_SID = account_sid
TWILIO_AUTH_TOKEN = auth_token
TWILIO_VIRTUAL_NUMBER = phone_twilio
TWILIO_VERIFIED_NUMBER = phone_to
my_email = EMAIL
my_password = PASSWORD
send_to

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self):
        pass