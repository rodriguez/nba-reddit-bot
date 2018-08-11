import praw
import os
from nba_players import players_dic

reddit = praw.Reddit(client_id='fFCCdbz1412TtQ', client_secret='KkSdtRChP6uq-fe2usK04GYttbk', username='Arod16', password='paugasol16', user_agent='testscript by /u/Arod15')

def clear():
    os.system('cls')

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
    action = input('Enter 0 if you want to clear the screen: ')
    if not int(action):
        clear()
main()