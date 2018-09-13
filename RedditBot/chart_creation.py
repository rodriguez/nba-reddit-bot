from redditbot import players_dic, start_time
import time
# code below taken from Python Tutorials at https://pythonspot.com/matplotlib-bar-chart/
# I am a novie programmer, so I feel more comfortable giving credit where it is deserved

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

players_comment = []

for x in players_dic:
    if players_dic[x][0] != 0:
        players_comment.append([players_dic[x][0], x])
players_comment.sort(reverse=True)
print(players_comment)
players = [x[1] for x in players_comment]
values = [x[0] for x in players_comment]
players = players[:10]
values = values[:10]
print(values)
y_pos = np.arange(len(players))

plt.barh(y_pos, values, align='center', alpha=0.5)
plt.yticks(y_pos, players)
plt.xlabel('Number of Comments')
plt.title('Frequency of Players in Comments')

print("--- %s seconds ---" % (time.time() - start_time))
plt.show()