import requests 

# Output multiple Game titles up to five, let user pick the correct option
# Run functions below 
userInput = str(input('\nPlease Enter a Game Title/Series: ')).capitalize()
response = requests.get(f'https://www.cheapshark.com/api/1.0/games?title={userInput}&limit=5')
json_data = response.json()
char = {'(': '', ')': '', "'": ''}

def steam1(): 

    if bool(json_data) == True:
        def testing():
            title = json_data[0:len(json_data)]
            test = []
            for i in range(0, len(title)):
                test.append(title[i]['external'])
                if i < 4:
                    print(title[i]['external'])
                else:
                    print(f'{title[i]["external"]}\n')
            print(test)
            
            def testing2():
                gameChoice = str(input("Which Game (Case Sensitive)!: "))
                if gameChoice in test:
                    a = test.index(gameChoice)
                    steam = json_data[a]['external'], json_data[a]['cheapest'], json_data[a]['thumb']
                    for k, v in char.items():
                        steam = str(steam).replace(k, v)
                        steam = str(steam).replace(',', ":", 1)
                    print(steam)
                    
                    def deals():
                        if str(json_data[a]['steamAppID']) == 'None':
                            print("\nThis Game Has No Steam ID.")
                        else:
                            if str(json_data[a]['cheapestDealID']) == 'None':
                                print(f"No Deal ID found!...Printing steam Link: https://store.steampowered.com/app/{json_data[a]['steamAppID']}")
                            else:
                                steam2 = json_data[a]['steamAppID']
                                steam3 = json_data[a]['cheapestDealID']
                                print(f'\nGiven Deal Link: https://store.steampowered.com/app/{steam2}/{steam3}')
                    deals()
                    
                else:
                    print("Game not in list. Restart Command")
               
            testing2()
        testing()
    else:
        print('No Game Data Found.')
    
steam1()
