import requests
from lxml import html

class Temperature:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        url = 'https://www.timeanddate.com/weather/' + self.country + '/' + self.city
        page = requests.get(url)
        content = html.fromstring(page.content)
        temp = content.xpath('//*[@id="qlook"]/div[2]/text()')[0]
        temp = ''.join([ch for ch in temp if ch.isdigit()])
        return int(temp)
