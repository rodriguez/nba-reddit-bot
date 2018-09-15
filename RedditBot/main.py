from redditbot import *
from nba_players import start_time
import time
def main():
    search_for_players_frontpage()
    clean_players_dic()
    prepare_payload()
    replace_comments_with_ratios()
    print("--- %s seconds ---" % (time.time() - start_time))
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
main() 