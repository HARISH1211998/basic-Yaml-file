import requests

url = "https://hubz.io"

response = requests.get(url)

if response.status_code == 200:
    print(f"the responce from the website {response.status_code}")
else:
    print(f"the responce from the website {response.status_code}")