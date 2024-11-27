import requests

url = input("Entrez l'url du site : ")
requests.get(url)

try:
    reponse = requests.get(url)
    reponse.raise_for_status()
except requests.exceptions.HTTPError as errh :
    print("Http Error : ", errh)
except requests.exceptions.ConnectionError as errc :
    print("Error connecting : ", errc )
except requests.exceptions.Timeout as errt :
    print("Timeout Error : ", errt)
except requests.exceptions.RequestException as err :
    print("OOps: Something Else", err)

""" print(reponse.text) """