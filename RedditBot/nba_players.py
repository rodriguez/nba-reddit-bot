# this file is for grabbing the names of every nba player (hopefully)

# import requests
# response = requests.get('https://stats.nba.com/players/list/')
# open('players', 'wb').write(response.content)
# print(response.status_code)
# print(response.text)

# Apparently, there was an easier way to do this; someone already had a JSON with the names.
# I took this JSON file from Nick Bottomley's (bttmly) project at https://github.com/bttmly/nba
import time
import json

start_time = time.time()

with open('players.json', 'r') as file:
    json_dic = json.load(file)

players_dic = {}

for player in json_dic:
    players_dic[player['firstName'] + ' ' + player['lastName']] = {'name-drops': 0, 'comments': []}
    
print('This code does run \n -------------')