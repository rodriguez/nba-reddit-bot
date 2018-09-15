import time
import json

from redditbot import *
from nba_players import start_time, players_dic
from chart_creation import create_chart


def write_dic_to_json(dic):  
    hello = json.dumps(dic)
    f = open("players_dic.json", "w")
    f.write(hello)
    f.close()
def read_json_to_dic():
    with open("players_dic.json") as file:
        dic = json.loads(file.read())
    return dic

def main():
    global players_dic
    players_dic = search_for_players_frontpage(players_dic)
    payload = prepare_payload(players_dic)
    api_results = get_sentiment_payload(payload)
    players_dic = clean_dic(players_dic)
    players_dic = replace_comments_with_ratios(players_dic, api_results)
    write_dic_to_json(players_dic)
    print(players_dic)
    pass_dic_for_chart(players_dic)
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
def test():
    global players_dic
    players_dic = read_json_to_dic()
    pass_dic_for_chart(players_dic)
    print("--- %s seconds ---" % (time.time() - start_time))
test()