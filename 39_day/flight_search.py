import requests
from API_CODE import *
API_KEY = tequila_api_key
import datetime as dt

class FlightSearch:


    def get_iata(self, city):
        url_flight = 'https://tequila-api.kiwi.com/locations/query'
        head = {'apikey': API_KEY}
        call = {
            'term': city,
            'location_types': 'city'

        }
        answer = requests.get(url=url_flight, params=call, headers=head)
        answer.raise_for_status()
        an = answer.json()['locations'][0]['code']
        return an

    def get_price(self, starting, ending):
        url_flight = 'https://tequila-api.kiwi.com/aggregation_search/price_per_city'
        head = {'apikey': API_KEY}
        today = dt.date.today()
        date_start = (today +dt.timedelta(1)).strftime('%d/%m/%Y')
        date_end =(today +dt.timedelta(180)).strftime('%d/%m/%Y')
        call = {
            'fly_from': starting,
            'fly_to': ending,
            'date_from': date_start,
            'date_to': date_end,
        }
        answer = requests.get(url=url_flight, params=call, headers=head)
        answer.raise_for_status()
        return answer.json()['data']
