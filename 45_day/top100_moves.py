from bs4 import BeautifulSoup
import requests

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
request = requests.get(url)
web_site = BeautifulSoup(request.text, "html.parser")
for tag in web_site.find_all(name='h3', class_="jsx-4245974604"):
    print(tag)
# print(web_site.find(h3))
