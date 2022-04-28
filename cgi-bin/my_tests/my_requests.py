import requests
responses = requests.get('https://randomuser.me/api/?results=2')
data = responses.json()
for item in data['results']:
    print(item['name']['last'])
