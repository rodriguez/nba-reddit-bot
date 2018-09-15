import praw
import os
import time
from indico import *
from nba_players import players_dic, start_time
reddit = praw.Reddit(client_id='fFCCdbz1412TtQ', client_secret='KkSdtRChP6uq-fe2usK04GYttbk', username='Arod16', password='paugasol16', user_agent='testscript by /u/Arod15')

payload = []

def clear():
    os.system('cls')

def replace_comments_with_ratios():
    i = 0
    api_results = get_sentiment_payload()
    results_length = len(api_results)
    for player in players_dic:
        if players_dic[player]['name-drops'] != 0 and i < results_length:
            num_comments = players_dic[player]['name-drops']
            next_i = i + num_comments
            comment_slice = api_results[i:next_i]
            print("comment slice: " + str(comment_slice))
            print("sum(comment_slice): " + str(sum(comment_slice)))
            print("len(comment_slice): " + str(len(comment_slice)))
            i = next_i
            # calculate average comment sentiment per player
            avg_ratio = sum(comment_slice) / len(comment_slice)
            players_dic[player]['comments'] = avg_ratio
    # print(players_dic)

def prepare_payload():
    for player in players_dic:
        if players_dic[player]['name-drops'] != 0:
            for comment in players_dic[player]['comments']:
                payload.append(comment)
                break
    print('PAYLOAD: \n')
    print(payload)

def get_sentiment_payload():
    api_results = indicoio.sentiment(payload)
    return api_results

def clean_players_dic():
    new_dic = {}
    global players_dic
    for player in players_dic:
        if players_dic[player]['name-drops'] != 0:
            new_dic[player] = players_dic[player]
    players_dic = new_dic
    print('PLAYERS_DIC: \n')
    print(players_dic)

def check_for_player(comment_string):
    for name in players_dic:
        # going to start with just full name substrings like 'Kyrie Irving'
        if name.lower() in comment_string.lower():
            players_dic[name]['name-drops'] += 1
            players_dic[name]['comments'].append(comment_string)

def search_for_players_frontpage():
    for submission in reddit.subreddit('NBA').hot(limit=20):
        submission.comments.replace_more(limit=0)
        flat_comments = submission.comments.list()
        for comment in flat_comments:
            # comment_id = comment.fullname.split('_')[1]
            check_for_player(comment.body)
    # check_nonzero_values()

def search_for_players_new():
    for comment in reddit.subreddit('NBA').stream.comments():
        comment_id = comment.fullname.split('_')[1]
        check_for_player(comment.body)


# Known Issues:
# 
# Don't try to be cool with trying to use the comment id as much as possible because the code won't run.
#  