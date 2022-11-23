import datetime
import json
import requests


# Presentera en meny för användaren där man först frå välja radiokanal
# När radiokanal blivit vald ska programmet skriva ut information om tablån för användaren
# Börja med channels vilka kanaler - lista med kanaler som innehåller id namn och beskrivning
# Använda för att fråga användaren vilken kanal
# Menu för kanalerna
# skicka p3 id till tablå url
def get_programs():
    response = requests.get('https://api.sr.se/v2/scheduledepisodes/index?format=json&channelid=132')
    print(response.content)

    data = response.json()

    # Ta emot ett id
    # från id ta fram info om kanalen kopplad till id
    # omvandla tiden till rätt format
    # programcategory, name, broadcastinfo
    for x in data['schedule']:
        info_name = x['title']
        temp = x['starttimeutc']
        startTimeInMillis = response.findall(r'\d+', temp)
        startTime = datetime.datetime.fromtimestamp(int(startTimeInMillis[0])/1000)
        startTime = startTime.strftime('%H:%M')
        endTime = x['endtimeutc']
        print('>',info_name, startTime, endTime)

    return info_name


def get_channels():
    # Get SR API content
    response = requests.get('https://api.sr.se/api/v2/channels/index?format=json&channelid=200')
    #print(response.text)

    data = response.json()

    # Write out channel name and channel id
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


