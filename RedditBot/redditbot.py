import praw
import os
from nba_players import players_dic

reddit = praw.Reddit(client_id='fFCCdbz1412TtQ', client_secret='KkSdtRChP6uq-fe2usK04GYttbk', username='Arod16', password='paugasol16', user_agent='testscript by /u/Arod15')
players_list = list(players_dic.keys())

def clear():
    os.system('cls')

def check_nonzero_values():
    for name in players_dic:
        if players_dic[name][0] != 0:
            print('----------')
            print('Name: ' + name)
            print('Value: ' + players_dic[name][0])
            print('First Comment: ' + str(players_dic[name])) 
            print('----------')
def check_for_player(comment_string):
    # Note: tried to get creative and check if a substring is a name
    # for word in comment_string.split():
    #     for key in players_dic:
    #         if word in key.split():
    #             players_dic[key] += 1
    for name in players_list:
        # going to start with just full name substrings like 'Kyrie Irving'
        if name.lower() in comment_string.lower():
            players_dic[name][0] = str(int(players_dic[name][0]) + 1)
            players_dic[name] += comment_string

def search_for_player(name):
    for submission in reddit.subreddit('NBA').hot(limit=5):
        submission.comments.replace_more(limit=0)
        flat_comments = submission.comments.list()
        for comment in flat_comments:
            check_for_player(comment.body)
    check_nonzero_values()
            

def main():
    print(players_dic)
    selection = input('Please enter a subreddit: ')
    selection = str(selection)
    if type(selection) is str:
        print('Hello World')
    for post in reddit.subreddit(selection).hot(limit=5):
        print('---------------')
        print(post.title)
        for comment in post.comments:
            print(comment.body)
            comment.save()
            print('You saved this comment: ' + str(comment.body))
            break
        print('---------------')
        break
# main()
search_for_player('Lebron James')
action = input('Enter 0 if you want to clear the screen: ')
if not int(action):
    clear()