import praw
import os
import time
import indicoio

from config import *
from chart_creation import create_chart

indicoio.config.api_key = INDICO_API_KEY
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
username=USERNAME, password=PASSWORD, user_agent=USER_AGENT)


def clear():
    # windows clear function in order to have tests in the terminal be more clean
    os.system('cls')

def replace_comments_with_ratios(dic, api_results):
    # to reduce runtime by n, I am looping through player keys and calculating which floats correspond to which players' comments
    i = 0
    results_length = len(api_results)
    for player in dic:
        if dic[player]['mentions'] != 0 and i < results_length:
            num_comments = dic[player]['mentions']
            next_i = i + num_comments
            comment_slice = api_results[i:next_i]
            i = next_i
            # calculate average comment sentiment per player
            avg_ratio = sum(comment_slice) / len(comment_slice)
            dic[player]['comments'] = avg_ratio
    return dic

def pass_dic_for_chart(dic):
    # possibly unnecessary helper function to create a graph from the dictionary
    create_chart(dic)

def prepare_payload(dic):
    # function that prepares the comments from players to be sent to the Indico API
    payload = []
    for player in dic:
        if dic[player]['mentions'] > 0:
            for comment in dic[player]['comments']:
                payload.append(comment)
    return payload

def get_sentiment_payload(payload):
    # helper function to retrieve the results of the API calls on the payload
    api_results = indicoio.sentiment(payload)
    return api_results

def clean_dic(dic):
    # returns dictionary of players with nonzero amount of comments
    new_dic = {}
    for player in dic:
        if dic[player]['mentions'] != 0:
            new_dic[player] = dic[player]
    dic = new_dic
    return dic

def check_for_players(dic, comment_string):
    # checks string for mentions of any player in dictionary
    for name in dic:
        # going to start with just full name substrings like 'Kyrie Irving'
        if name.lower() in comment_string.lower():
            dic[name]['mentions'] += 1
            dic[name]['comments'].append(comment_string)
        # only do this for one player -- unit test

def search_for_players_frontpage(dic):
    # scraping function for subreddit frontpage
    for submission in reddit.subreddit('NBA').hot(limit=20):
        submission.comments.replace_more(limit=0)
        flat_comments = submission.comments.list()
        for comment in flat_comments:
            check_for_players(dic, comment.body)
    dic = clean_dic(dic)
    return dic

def search_for_players_new(dic):
    for comment in reddit.subreddit('NBA').stream.comments():
        comment_id = comment.fullname.split('_')[1]
        check_for_players(dic, comment.body)


# Known Issues:
# 
# Don't try to be cool with trying to use the comment id as much as possible because the code won't run.
#  