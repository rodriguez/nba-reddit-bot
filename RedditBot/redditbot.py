import praw
import os
import time
from indico import *
from config import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT
from chart_creation import create_chart

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)


def clear():
    os.system('cls')

def replace_comments_with_ratios(dic, api_results):
    i = 0
    results_length = len(api_results)
    for player in dic:
        if dic[player]['name-drops'] != 0 and i < results_length:
            num_comments = dic[player]['name-drops']
            next_i = i + num_comments
            comment_slice = api_results[i:next_i]
            i = next_i
            # calculate average comment sentiment per player
            avg_ratio = sum(comment_slice) / len(comment_slice)
            dic[player]['comments'] = avg_ratio
    return dic

def pass_dic_for_chart(dic):
    create_chart(dic)
def prepare_payload(dic):
    payload = []
    for player in dic:
        if dic[player]['name-drops'] != 0:
            for comment in dic[player]['comments']:
                payload.append(comment)
                break
    return payload

def get_sentiment_payload(payload):
    api_results = indicoio.sentiment(payload)
    return api_results

def clean_dic(dic):
    new_dic = {}
    for player in dic:
        if dic[player]['name-drops'] != 0:
            new_dic[player] = dic[player]
    dic = new_dic
    return dic

def check_for_player(dic, comment_string):
    for name in dic:
        # going to start with just full name substrings like 'Kyrie Irving'
        if name.lower() in comment_string.lower() and dic[name]['bool'] == False:
            dic[name]['name-drops'] += 1
            dic[name]['comments'].append(comment_string)
            dic[name]['bool'] = True

def search_for_players_frontpage(dic):
    for submission in reddit.subreddit('NBA').hot(limit=20):
        submission.comments.replace_more(limit=0)
        flat_comments = submission.comments.list()
        for comment in flat_comments:
            check_for_player(dic, comment.body)
    dic = clean_dic(dic)
    return dic

def search_for_players_new(dic):
    for comment in reddit.subreddit('NBA').stream.comments():
        comment_id = comment.fullname.split('_')[1]
        check_for_player(dic, comment.body)


# Known Issues:
# 
# Don't try to be cool with trying to use the comment id as much as possible because the code won't run.
#  