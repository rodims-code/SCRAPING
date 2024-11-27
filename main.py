import requests

response = requests.get("https://www.google.com")

with open("files_html/index.html", "w") as f :
    f.write(response.text)



