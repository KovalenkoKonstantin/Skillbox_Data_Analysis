import urllib.request as req
API_KEY = "5eff49003b6447e6a29143652221707"

days = 3
url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=Moscow&days={days}"

session = req.urlopen(url)
response = session.read().decode()

print(response)

session.close()

with req.urlopen(url) as session:
  response1 = session.read().decode()

response1

import json

data = json.loads(response)
data
