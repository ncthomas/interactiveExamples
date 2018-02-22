
from __future__ import print_function
import sys
import string
import pandas as pd
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection 
import time

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

def on_move(event):

    if event.inaxes:
        x_coords.append(event.xdata)
        y_coords.append(event.ydata)

        ax.plot(x_coords[-3:-1], y_coords[-3:-1], color='black')
        plt.draw()

def on_click(event):

    x_clicks.append(event.xdata)
    y_clicks.append(event.ydata)

def euclidean_distance(x1,y1,x2,y2):

    return np.sqrt((x1-x2)**2+(y1-y2)**2)

def plot_store(layout_data, ax):

    x_list = layout_data['xmin'].tolist()
    y_list = layout_data['ymin'].tolist()
    width_list = [xmax-xmin for xmin, xmax in zip(layout_data['xmin'], layout_data['xmax'])]
    depth_list = [ymax-ymin for ymin, ymax in zip(layout_data['ymin'], layout_data['ymax'])]
    angle_list = layout_data['angle'].tolist()
    bays =  [ patches.Rectangle( (x, y), width, depth, angle=angle ) for (x,y,width,depth,angle) in zip(x_list, y_list, width_list, depth_list,angle_list)]
    pc = PatchCollection(bays, facecolor='orange', edgecolor='black', linewidth=2)
    ax.add_collection(pc)
    ax.scatter(0, 5, color='red', s=300)
    ax.set_xlim([-1,10])
    ax.set_ylim([-1,10])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

layout_data = pd.read_csv('../../data/box_data.csv')

## RUN
run = True
while run:

    x_coords = []
    y_coords = []
    x_clicks = []
    y_clicks = []

    ## TRACK MOUSE MOVEMENT AND CLICKS
    fig, ax = plt.subplots()
    plot_store(layout_data, ax)
    fig.canvas.draw()
    carry_on = False
    while carry_on == False:
        if plt.waitforbuttonpress(timeout=6000):
            carry_on = True
    start = time.time()
    go_text = ax.text(0, 10, 'Go!', fontsize=20, horizontalalignment='left', verticalalignment='center', fontweight='bold')
    fig.canvas.draw()
    moving = plt.connect('motion_notify_event', on_move)
    clicking = plt.connect('button_press_event', on_click)

    num_clicks_allowed = 3
    while len(x_clicks) < num_clicks_allowed:
        plt.waitforbuttonpress(timeout=6000)
        fig.canvas.draw()

    fig.canvas.mpl_disconnect(moving)
    fig.canvas.mpl_disconnect(clicking)

    end = time.time()
    total_time = np.round(end-start, 2)

    plot_store(layout_data, ax)
    fig.canvas.draw()
    plt.pause(0.01)

    ## CHECK RESULTS
    success = True
    if success:
        for x1, y1 in zip(x_coords, y_coords):
            check = len(layout_data[(layout_data.xmin <= x1) & (layout_data.ymin <= y1) & (layout_data.xmax >= x1) & (layout_data.ymax >= y1)])
            if check > 0:
                success = False
    if success:
        label = 'Pass'
    else:
        label = 'Fail'

    ## PLOT RESULTS
    go_text.remove()
    fig.canvas.draw()
    if success:
        ax.plot(x_coords, y_coords, color='green')
    else:
        ax.plot(x_coords, y_coords, color='red')
    ax.plot(x_clicks, y_clicks, 'o', color='black')
    if success:
        ax.text(0, 9, label + ': Time = '+str(total_time)+str(' seconds'), fontsize=20, fontweight='bold', color='green')
    else:
        ax.text(0, 9, label + ': Time = '+str(total_time)+str(' seconds'), fontsize=20, fontweight='bold', color='red')

    fig.canvas.draw()
    plt.show()
