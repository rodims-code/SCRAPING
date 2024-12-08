import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Fooction pour parcourrir recursivement l'arbre DOM
def traver_dom(element, level=0) :
    #Afficher l'element actuel
    if element.name : 
        print(f"{'' * level}<{element.name}>")

    # Si l'element a des enfants, les parcourrir egalement
    if hasattr(element, 'children') :
        for child in element.children :
            traver_dom(child, level + 1)

traver_dom(soup)