
# code below taken from Python Tutorials at https://pythonspot.com/matplotlib-bar-chart/
# I am a novice programmer, so I feel more comfortable giving credit where it is deserved

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

players_value_pairs = []

def create_chart_players(dic):
    for player in dic:
        players_value_pairs.append([dic[player]['comments'], player])
    players = [x[1] for x in players_value_pairs]
    values = [x[0] for x in players_value_pairs]
    print(players)
    print(values)
    y_pos = np.arange(len(players))

    plt.barh(y_pos, values, align='center', alpha=None)
    plt.yticks(y_pos, players)
    plt.xlabel('Probability of Positive Comments over Negative')
    plt.title('/r/NBA Comment Analysis on Players')
    plt.show()

def create_chart_player(dic, player_name):
    player_values_pair = [dic[player_name]['comments'], player_name]
    player = [player_name]
    values = player_values_pair[0]
    num_comment = [x for x in range(1, len(values) + 1)]
    print(player)
    print(values)
    plt.rcParams["font.size"] = 16
    y_pos = np.arange(len(values))
    plt.bar(y_pos, values, align='center', alpha=None)
    plt.xticks(y_pos, num_comment)
    title = "/r/NBA Comment Analysis on " + player_name
    plt.xlabel(title)
    plt.title('Probability of Positive Comments over Negative')
    plt.show()