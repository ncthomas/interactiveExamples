
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['keymap.all_axes'] = ''
plt.rcParams['keymap.zoom'] = ''
plt.rcParams['keymap.xscale'] = ''
plt.rcParams['keymap.yscale'] = ''
plt.rcParams['keymap.save'] = ''
plt.rcParams['keymap.all_axes'] = ''
plt.rcParams['keymap.quit_all'] = ''
plt.rcParams['keymap.pan'] = ''
plt.rcParams['keymap.home'] = ''
plt.rcParams['keymap.grid_minor'] = ''
plt.rcParams['keymap.grid'] = ''
plt.rcParams['keymap.fullscreen'] = ''
plt.rcParams['keymap.forward'] = ''
plt.rcParams['keymap.back'] = ''
plt.rcParams['toolbar'] = 'None'

matplotlib.rcParams['font.sans-serif'] = "Ubuntu"

def get_nearest_point(x, y, data):

    dists = [ np.sqrt((x-xpoint)**2 + (y-ypoint)**2) for xpoint, ypoint in zip(data['total_bill'], data['tip']) ]
    min_dist_index = np.argmin(dists)

    return min_dist_index

def on_click(event):

    ax.clear()
    ax.scatter(data['total_bill'], data['tip'], color='black')
    x = event.xdata
    y = event.ydata
    index = get_nearest_point(x,y,data)
    ax.scatter(data.loc[index,'total_bill'], data.loc[index,'tip'], color='red')
    ax.text(x+0.5, y+0.5, 'Gender : ' + data.loc[index,'sex'] + '\n Smoker : ' + data.loc[index,'smoker'], horizontalalignment='left', backgroundcolor='yellow')
    ax.set_xlabel('Total Bill (£)')
    ax.set_ylabel('Tip (£)')
    fig.canvas.draw()

data = pd.read_csv('../../data/tips_data.csv')

fig, ax = plt.subplots()
ax.clear()
clicking = plt.connect('button_press_event', on_click)
plt.show()
