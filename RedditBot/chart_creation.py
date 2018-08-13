from redditbot import players_dic

# code below taken from Python Tutorials at https://pythonspot.com/matplotlib-bar-chart/
# I am a novie programmer, so I feel more comfortable giving credit where it is deserved

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
# players = [x for x in players_dic]
graph_list = []
for x in players_dic:
    if players_dic[x] != 0:
        graph_list.append(x)

y_pos = np.arange(len(graph_list))
values = [players_dic[x][0] for x in graph_list]
 
plt.bar(y_pos, values, align='center', alpha=0.5)
plt.xticks(y_pos, graph_list)
plt.ylabel('Number of Comments')
plt.title('Frequency of Players in Comments')
 
plt.show()