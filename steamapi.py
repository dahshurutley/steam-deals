
import json
import requests 
from bs4 import BeautifulSoup
import json

# Create a Program that Returns Data entry of game Titles and Price
# In regard to user search 
# Refereance: {"gameID":"146197","steamAppID":"348360","cheapest":"3.14",
# "cheapestDealID":"Z4c%2BSbJ%2BLxNMisUoEnB%2Fq5b1I%2B2VT%2FVSmZTwO6mQTqs%3D",
# "external":"Doodle God","internalName":"DOODLEGOD",
# "thumb":"https:\/\/cdn.cloudflare.steamstatic.com\/steam\/apps\/348360\/capsule_sm_120.jpg?t=1629373614"},

def steam1(): 

    userInput = str(input('\nPlease Enter a Game Title/Series: ')).capitalize()
    response = requests.get(f'https://www.cheapshark.com/api/1.0/games?title={userInput}')
    json_data = response.json()
    test = {'(': '', ')': '', "'": ''}
    
    if bool(json_data) == False:
        print("No Games Found!")
    else:
        # Json "null" = Python 'None', convert to string and print based on Boolean Values
        if str(json_data[0]['steamAppID']) == 'None':
            print('No SteamAppID found!')   
        else:
            def func(): 
                # Itterate in for loop for each key pair in dict. 
                steam = json_data[0]['external'], json_data[0]['cheapest'], json_data[0]['thumb']
                for k, v in test.items():
                    steam = str(steam).replace(k, v)
                steam = str(steam).replace(',', ":", 1)
                return steam
            def deals():
                if str(json_data[0]['cheapestDealID']) == 'None':
                    print("No Deal ID found!...Printing steam Link: ")
                else:
                    steam2 = json_data[0]['steamAppID']
                    steam3 = json_data[0]['cheapestDealID']
                    print(f'\nGiven Deal Link: https://store.steampowered.com/app/{steam2}/{steam3}')
            print(f'\n{func()}')
            deals()


steam1()