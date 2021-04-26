from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FLY_FROM = 'KZN'
CITY = 'Kazan'
flights = FlightSearch()
data = DataManager()
notify = NotificationManager()


# filling index
def fill_index():
    cities, price = data.get_rows()
    IATA = []
    for city in cities:
        IATA.append(flights.get_iata(city))
    for z in range(len(IATA)):
        data.put_iata(IATA[z], z)


def get_minimum(where):
    fly = flights.get_price(FLY_FROM, where)
    for value in fly:
        return fly[value]


def check_if_lower():
    cities, price = data.get_rows()
    iata = data.get_iata()
    for g in range(len(cities)):
        current_price = get_minimum(iata[g])
        if current_price < price[g]:
            print(current_price, price[g])
            notify.send_message(FLY_FROM, CITY,iata[g], cities[g], current_price)


check_if_lower()
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
