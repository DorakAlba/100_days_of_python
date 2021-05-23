from games import game_pages
from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
DRIVER_PATH = '..\chromedriver.exe'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


class ParsedGame:
    def __init__(self, url):
        self.url = url
        self.name = url.split("game/")[1]
        self.url_sellers = f"{url}sellers/"
        print(self.url_sellers)
        driver.get( self.url_sellers)
        # print(driver.page_source)
        h1 = driver.find_elements_by_class_name('feed_message')
        for element in h1:
            print(element.text)
        driver.quit()

        # self.driver = webdriver.PhantomJS()
        # self.driver.get(self.url_sellers)
        # self.response = session.body()
        # self.response = requests.get(url=self.url_sellers, headers=header)
        # self.soup = BeautifulSoup(self.response.text, 'html.parser')
        # print (self.soup)

    def find_messages(self):
        # for tag in self.soup.find_all(class_='feed'):
        #     print(tag.get_text())
        # print(g)
        # classes = []
        # for element in self.soup.find_all(class_=True):
        #     classes.extend(element["class"])
        # print(classes)
        p_element = self.driver.find_element_by_id(class_='feed_message')
        print(p_element)



# for game in game_pages:
g = ParsedGame(game_pages[2])
# g.find_messages()
