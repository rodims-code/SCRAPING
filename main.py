import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='product_pod')
for article in articles : 
    links = article.find_all('a')
    if len(links) >= 2 :
        link = links[1]
        print(link.get('title'))