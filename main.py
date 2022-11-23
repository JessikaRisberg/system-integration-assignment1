import json
import requests


# Presentera en meny för användaren där man först frå välja radiokanal
# När radiokanal blivit vald ska programmet skriva ut information om tablån för användaren
# Börja med channels vilka kanaler - lista med kanaler som innehåller id namn och beskrivning
# Använda för att fråga användaren vilken kanal
# Menu för kanalerna
# skicka p3 id till tablå url
def get_programs():
    response = requests.get('https://api.sr.se/api/v2/programs/index?format=json&channelid=200')

    data = response.json()

    # programcategory, name, broadcastinfo
    for x in data['programs']:
        info_name = x['name']
        info_time = x['broadcastinfo']
        print('>',info_name, info_time)

    return x

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


def channels_menu():
    # Get all channels
    channels = get_channels()
    # Put all channel names in a menu
    menu = {
        "kanal": channels['name'],
        "id": channels['id'],
    }

    # choose channel
    # use the channel id to get information
    print(menu)
    keep_playing = True
    while keep_playing:
        print(menu)
        choice = int(input("val: "))

       # if choice == 1:


if __name__ == '__main__':
    get_programs()
    #get_channels()
    #channels_menu()


