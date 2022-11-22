import json
from urllib.request import urlopen
import requests
import xmltodict
from requests.exceptions import HTTPError

# Get SR api channels
#response = requests.get("http://api.sr.se/api/v2/channels")
#print(response.content)
#print(response.status_code)

# convert from XML to JSON
#dict_data = xmltodict.parse(response.content)
#json_data = json.dumps(dict_data)

#print(json_data[10])


#print(json_data)
#data = json_data["channelid"]
#print(data['name'])

# Get SR API content
r = requests.get('https://api.sr.se/api/v2/programs/index?format=json&channelid=200')
print(r.text)

data = r.json()
first_hit = data['channels']
print()
print(first_hit['description'])

# Presentera en meny för användaren där man först frå välja radiokanal
# När radiokanal blivit vald ska programmet skriva ut information om tablån för användaren
#