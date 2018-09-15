from redditbot import *
from nba_players import start_time, players_dic
from chart_creation import create_chart
import time

def main():
    global players_dic
    print(players_dic['Al Horford']['comments'])
    players_dic = search_for_players_frontpage(players_dic)
    print(players_dic['Al Horford']['comments'])
    payload = prepare_payload(players_dic)
    print(players_dic['Al Horford']['comments'])
    api_results = get_sentiment_payload(payload)
    print(players_dic['Al Horford']['comments'])
    players_dic = clean_dic(players_dic)
    print(players_dic['Al Horford']['comments'])
    players_dic = replace_comments_with_ratios(players_dic, api_results)
    print(players_dic['Al Horford']['comments'])
    # print(players_dic)
    # pass_dic_for_chart(players_dic)
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
main() 