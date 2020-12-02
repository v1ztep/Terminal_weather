import requests

CITIES = ('Лондон', 'Шереметьево', 'Череповец')
PARAMS = {'nTqm':'', 'lang': 'ru'}

url_template = 'http://wttr.in/{}'

for city in CITIES:
    url = url_template.format(city)
    response = requests.get(url, params=PARAMS)
    response.raise_for_status()
    print(response.text)

