import requests

reponse = requests.get("https://www.google.com")

print(reponse.text)