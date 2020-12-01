import requests

CITIES = ('Лондон', 'Шереметьево', 'Череповец')
PARAMS = 'mpqT&lang=ru'

url_template = 'http://wttr.in/{}?{}'

for city in CITIES:
    url = url_template.format(city, PARAMS)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

