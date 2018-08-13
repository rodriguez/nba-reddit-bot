import praw
import os
from nba_players import players_dic

reddit = praw.Reddit(client_id='fFCCdbz1412TtQ', client_secret='KkSdtRChP6uq-fe2usK04GYttbk', username='Arod16', password='paugasol16', user_agent='testscript by /u/Arod15')

def clear():
    os.system('cls')

def check_nonzero_values():
    for name in players_dic:
        if players_dic[name][0] != 0:
            print('----------')
            print('Name: ' + name)
            print('Value: ' + str(players_dic[name][0]))
            print('\n')
            for comment_id in players_dic[name][1:]: # excludes the first item which is the counter
                comment = reddit.comment(comment_id)
                print('Comment: ' + comment.body)
                print('Comment Score: ' + str(comment.score))
def check_for_player(comment_string, comment_id):
    # Note: tried to get creative and check if a substring is a name
    # for word in comment_string.split():
    #     for key in players_dic:
    #         if word in key.split():
    #             players_dic[key] += 1
    for name in players_dic:
        # going to start with just full name substrings like 'Kyrie Irving'
        if name.lower() in comment_string.lower():
            players_dic[name][0] += 1
            players_dic[name].append(comment_id)

def search_for_players_frontpage():
    for submission in reddit.subreddit('NBA').hot(limit=5):
        submission.comments.replace_more(limit=0)
        flat_comments = submission.comments.list()
        for comment in flat_comments:
            comment_id = comment.fullname.split('_')[1]
            check_for_player(comment.body, comment_id)
    check_nonzero_values()

def search_for_players_new():
    for comment in reddit.subreddit('NBA').stream.comments():
        comment_id = comment.fullname.split('_')[1]
        check_for_player(comment.body, comment_id)
        print(comment.body)

def main():
    search_for_players_frontpage()
    # action = input('Enter 0 if you want to clear the screen: ')
    # if not int(action):
    #     clear()
main()

# Known Issues:
# 
# Don't try to be cool with trying to use the comment id as much as possible because the code won't run.
#  