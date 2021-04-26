import requests
from API_CODE import *

API_CODE = sheety_token


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_iata(self):
        head = {"Authorization": API_CODE}
        url = 'https://api.sheety.co/888188e34cf00cfe406cfdb85af894be/flightDeals/prices'
        city = requests.get(url=url, headers=head)
        city = city.json()
        el = [v['iataCode'] for v in city['prices']]
        return el

    def get_rows(self):
        head = {"Authorization": API_CODE}
        url = 'https://api.sheety.co/888188e34cf00cfe406cfdb85af894be/flightDeals/prices'
        city = requests.get(url=url, headers=head)
        city = city.json()
        el = [v['city'] for v in city['prices']]
        el2 = [v['lowestPrice'] for v in city['prices']]
        return el, el2

    def put_iata(self, iata, index):
        head = {"Authorization": API_CODE}
        url = f'https://api.sheety.co/888188e34cf00cfe406cfdb85af894be/flightDeals/prices/{index + 2}'
        body = {
            'price': {
                # 'City': 'Paris',
                'iataCode': iata
            }
        }
        req = requests.put(url=url, headers=head, json=body)
        req.raise_for_status()
# a = DataManager()
# q,w =a.get_rows()
# print(w)
