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
        starttimeutc = x['starttimeutc']
        endtimeutc = x['endtimeutc']
        startTime = datetime.datetime.fromtimestamp(int(starttimeutc[6:-2]) / 1000).strftime('%H:%M')
        endTime = datetime.datetime.fromtimestamp(int(endtimeutc[6:-2]) / 1000).strftime('%H:%M')
        print('>', startTime, '-', endTime, '--', info_name)

    return info_name, startTime


def get_channels():
    # Get SR API content
    response = requests.get('https://api.sr.se/api/v2/channels/index?format=json')
    #print(response.text)

    data = response.json()

    channel_dict = {}
    # Write out channel name and channel id
    for data in data['channels']:
        channel_name = data['name']
        channel_id = data['id']
        channel_dict[channel_name] = channel_id
        #print(channel_dict)

    return channel_dict

# lista som håller flera saker t.ex. lägga llt i en lista, varje sak i listan är kanal som dict
def write_out_channels_for_menu():
    channels = get_channels()

    for key in channels:
        menuChocie = ('>', key)
        #print('>', key)
    return menuChocie



def channels_menu():
    # Get all channels
    # Hämtar alla stationer
    channels = get_channels()

    # Put all channels from channel_dict in list
   # keyList = list(channels.keys())






    keep_playing = True
    while keep_playing:
        for key in channels:
            menuChocie = '>' + ' ' + key
            print(menuChocie)
        # välj station
        choice = input("välj kanal: ")

        if choice in menuChocie:
            #get_programs(channels)
            print("val: ", choice)
            print(menuChocie[key])


    #skall det göras en if else till varje kanal?
    # behöver man installera packet i python för c



if __name__ == '__main__':
    get_programs()
    #get_channels()
    #channels_menu()
    #write_out_channels_for_menu()

