from bs4 import BeautifulSoup
import requests
url=("https://www.regexsoftware.com/")
data = requests.get(url).text
print(data)
