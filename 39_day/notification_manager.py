from twilio.rest import Client
from API_CODE import *


class NotificationManager:
    def send_message(self, iata_d, city_d, iata,city,price):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"from {city_d}-{iata_d} to {city}-{iata} Low price alert! {price}$",
            from_=phone_twilio,
            to=phone_to
        )

        print(message.sid)
