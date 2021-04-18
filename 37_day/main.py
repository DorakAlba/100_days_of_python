import requests
import datetime as dt

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN =
USERNAME =
GRAPH = 'graph1'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     'id': 'graph1',
#     'name': 'reading',
#     'unit': '30 min',
#     'type': 'float',
#     'color': 'sora'
# }
headers = {
    'X-USER-TOKEN': TOKEN
}
# answer = requests.post(url=graph_endpoint, json=graph_config, headers =headers)
# print(answer.json())
graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"


def i_read_hard(how_long):
    today = dt.datetime.now()
    todata = (f"{str(today.year)}{today.month:02d}{today.day:02d}")
    print(how_long)
    pixel_config = {
        'date': todata,
        'quantity': how_long,
    }
    answer = requests.post(url=graph_pixel, json=pixel_config, headers=headers)
    print(answer.text)


# i_read_hard('2')

def update_date(date, how_long):
    graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
    print(graph_pixel)
    pixel_config = {
        'quantity': how_long,
    }
    answer = requests.put(url=graph_pixel, json=pixel_config, headers=headers)
    print(answer.text)

def delete_date (date):
    graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
    print(graph_pixel)

    answer = requests.delete(url=graph_pixel, headers=headers)
    print(answer.text)
delete_date ('20210418')
