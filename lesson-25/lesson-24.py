import requests
apikey = 'de1c381585f10ce959c30eebf0f74dbc'
units = 'metric'
city = 'Москва'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={apikey}&units={units}'


r = requests.get(url)

print(r.json()['main']['temp'])