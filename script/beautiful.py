import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extract and print the titles of all articles
for title in soup.find_all('h1'):
    print(title.get_text())
