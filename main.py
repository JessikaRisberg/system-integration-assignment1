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
    #print(response.text)

    data = response.json()

    # Write out channle name and channel id
    for x in data['channels']:
        channel_name = x['name']
        channel_id = x['id']
        print(channel_name, channel_id)

    return x

#def channels_menu():
 #   for key in get_channels():
  #      option = key, '--', get_channels()
   #     return option

    #keep_playing = True
    #while keep_playing:
     #   print(option)
      #  choice = int(input("val: "))


if __name__ == '__main__':
   get_channels()
   # while (True):
    #    channels_menu()
     #   option = input('Enter your choice: ')


