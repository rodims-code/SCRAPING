import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


body = soup.find('body')

print(body.prettify())