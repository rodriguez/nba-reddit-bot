# this file is for grabbing the names of every nba player (hopefully)
# Apparently, there was an easier way to do this; someone already had a JSON with the names.
# I took this JSON file from Nick Bottomley's (bttmly) project at https://github.com/bttmly/nba

import time
import json

start_time = time.time()
players_dic = {}

with open('players.json', 'r') as file:
    json_dic = json.load(file)


for player in json_dic:
    players_dic[player['firstName'].upper() + ' ' + player['lastName'].upper()] = {'mentions': 0, 'comments': []}
    
