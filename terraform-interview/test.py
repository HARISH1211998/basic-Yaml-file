import requests
from bs4 import BeautifulSoup

url = "https://hubz.io"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for title in soup.find_all('h1'):
    print(title.get_text())

