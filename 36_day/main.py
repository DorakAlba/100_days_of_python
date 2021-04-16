import requests
import datetime as dt
import os
from twilio.rest import Client
phone_number = '+18153174067'
yesterday = dt.datetime.now()
year = yesterday.year
month = yesterday.month
day_1d = int(yesterday.day) - 1
day_2d = int(yesterday.day) - 2
hour_1d = "20:00:00"
day1 = f"{year}-{month:02d}-{day_1d:02d} {hour_1d}"
day2_search = f"{year}-{month:02d}-{day_2d:02d}"
day2 = f"{year}-{month:02d}-{day_2d:02d} {hour_1d}"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = 'Z1MA0S16VJUJWB0O'
TWILLIO_AUTH = os.environ.get('TWILLIO_AUTH')
TWILLIO_SID = os.environ.get("TWILLIO_SID")
NEWS_API_KEY = 'e46f074e989249109993204c2ec47666'
URL = 'https://www.alphavantage.co/query?'
call_val = {'symbol': STOCK,
            'function': 'TIME_SERIES_INTRADAY',
            'interval': '60min',
            'apikey': API_KEY,
            }
NEWS_URL = 'https://newsapi.org/v2/everything?'
news_val = {'q': STOCK,
            'from': day2_search,
            'sort': 'popularity',
            'apiKey': NEWS_API_KEY,
            }


def send_message(phone_number, messages, change, change_sign, company, TWILIO_AUTH=TWILLIO_AUTH, TWILLIO_SID=TWILLIO_SID):
    client = Client(TWILLIO_SID, TWILIO_AUTH)
    if change_sign == 'Plus':
        change_sign = '🔼'
    else:
        change_sign = '🔽'

    message = client.messages.create(
        body=f"{company}:  {change_sign}{change}% \n {messages[0]} \n {messages[1]} \n {messages[2]}",
        from_=phone_number,
        to='+796558000'
    )
    print(message.status)


request = requests.get(url=URL, params=call_val)
request.raise_for_status()
value = request.json()['Time Series (60min)']
value_1d = value[day1]
value_2d = value[day2]

open_1 = int(float(value[day1]['1. open']))
close_2 = int(float(value[day2]['4. close']))

change = abs(open_1 - close_2) / (open_1 / 100)

if change > 5:
    if open_1 - close_2 < 0:
        change_sign = 'Minus'
    else:
        change_sign = 'Plus'
    request2 = requests.get(url=NEWS_URL, params=news_val)
    request2.raise_for_status()
    news = request2.json()

    articles = []
    for article in range(3):
        articles.append(news['articles'][article]['description'])
    print(articles)
    send_message(phone_number, articles, change, change_sign,COMPANY_NAME)

