from redditbot import *
from nba_players import start_time, players_dic
from chart_creation import create_chart
import time

def main():
    global players_dic
    players_dic = search_for_players_frontpage(players_dic)
    payload = prepare_payload(players_dic)
    api_results = get_sentiment_payload(payload)
    players_dic = replace_comments_with_ratios(players_dic, api_results)
    pass_dic_for_chart(players_dic)
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
main() 