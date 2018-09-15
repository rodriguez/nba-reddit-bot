from redditbot import *
from nba_players import start_time
from chart_creation import create_chart
import time

def main():
    search_for_players_frontpage()
    prepare_payload()
    replace_comments_with_ratios()
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
main() 