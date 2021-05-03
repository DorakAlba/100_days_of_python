from bs4 import BeautifulSoup
import requests

request = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(request.text, "html.parser")
points = []
for tag in soup.find_all(class_='score'):
    points.append(int(tag.getText().split()[0]))
most_popular = points.index(max(points))

article = []
for tag in soup.find_all(class_='storylink'):

    article.append((tag.getText(),tag.get('href')))
print(article[most_popular+1])
# with open('website.html', 'r') as a:
#     content = a.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
