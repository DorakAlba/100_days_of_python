import requests
import os
from twilio.rest import Client
account_sid = os.environ.get('ACCOUD_SSID')
auth_token = os.environ.get('AUTH_KEY')
API_KEY = os.environ.get('WEATHER_API')
latitude = 4.4
longitude = 68.342371
values = {'lat': latitude,
          'lon': longitude,
          "appid": API_KEY,
          "exclude":'current,minutely,daily'}
OMW_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall?'
call = requests.get(
    url=OMW_Endpoint, params=values)
call.raise_for_status()
weather_data = call.json()
bad_weather = False
for hour in range (12):
    if 700 > int(weather_data['hourly'][hour]['weather'][0]['id']):
        bad_weather = True
if bad_weather:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to be rainy☔",
        from_='+181531xxxx',
        to='+79655xxxxx)
    print (message.status)