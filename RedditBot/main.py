import time
import json

from redditbot import *
from nba_players import start_time, players_dic


def write_dic_to_json(dic, player_name=None):  
    temp = json.dumps(dic)
    if player_name is None:
        f = open("players_dic.json", "w")
    else:
        f = open("player_dic.json", "w")
    f.write(temp)
    f.close()

def read_json_to_dic(player_name=None):
    if player_name is not None:
        command = open("player_dic.json")
    else:
        command = open("players_dic.json")
    with command as file:
        dic = json.loads(file.read())
    return dic

def return_time():
    print("--- %s seconds ---" % (time.time() - start_time))

def init():
    # initial test that will grab fresh data, use API calls to analyze the data, create new graph
    global players_dic
    players_dic = search_sub_frontpage(players_dic)
    players_dic = clean_dic(players_dic)
    payload = prepare_payload(players_dic)
    api_results = get_sentiment_payload(payload)
    players_dic = replace_comments_with_ratios(players_dic, api_results)
    write_dic_to_json(players_dic)
    pass_dic_for_chart(players_dic)
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
def test():
    # runs program on data that is already gathered
    global players_dic
    players_dic = read_json_to_dic()
    pass_dic_for_chart(players_dic)
    return_time()
def unit_init():
    global players_dic
    players_dic_lower = {}
    for player in players_dic:
        players_dic_lower[player.lower()] = player
    raw_name = input('Please enter a name: ').lower()
    name = players_dic_lower[raw_name]
    player_dic = {}
    player_dic[name] = {'mentions': 0, 'comments': []}
    player_dic = search_sub_frontpage(player_dic, name)
    player_payload = prepare_payload(player_dic, name)
    player_sentiments = get_sentiment_payload(player_payload)
    player_dic = replace_comments_with_ratios(player_dic, player_sentiments, name)
    write_dic_to_json(player_dic, name)
    pass_dic_for_chart(player_dic, name)
    return_time()
def unit_test():
    name = 'LeBron James'
    player_dic = read_json_to_dic(name)
    pass_dic_for_chart(player_dic, name)
    return_time()
unit_test()