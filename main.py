import json
import requests

# Presentera en meny för användaren där man först frå välja radiokanal
# När radiokanal blivit vald ska programmet skriva ut information om tablån för användaren
# Börja med channels vilka kanaler - lista med kanaler som innehåller id namn och beskrivning
# Använda för att fråga användaren vilken kanal
# Menu för kanalerna
# skicka p3 id till tablå url
def get_channels():
    # Get SR API content
    response = requests.get('https://api.sr.se/api/v2/channels/index?format=json&channelid=200')
    print(response.text)

    data = response.json()
    first_hit = data['channels'][1]
    print(first_hit)
    print(first_hit['name'])
    for x in data['channels']:
        print(x['name'])

    return x



if __name__ == '__main__':
    get_channels()
