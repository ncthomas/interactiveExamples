import tkinter
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import seaborn as sns
import numpy as np
import pandas as pd

class InteractiveDemo(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.show()
        self.initialise()

    def initialise(self):

        ## LABEL FRAMES
        ###############
        frameTopRow = tkinter.LabelFrame(self)
        frameAbout = tkinter.LabelFrame(self, text=" About ")

        ## LABELS
        #########
        aboutLabel = tkinter.Label(frameAbout, text=" Developed by Niclas Thomas niclas.thomas@gmail.com")

        # BUTTONS AND ENTRY FIELDS
        ##########################
        openButton = tkinter.Button(frameTopRow, text="Browse", command=self.on_open)
        plotButton = tkinter.Button(frameTopRow, text="Plot", command=self.show_plot)
        genderButton = tkinter.Button(frameTopRow, text="By Gender", command=self.show_gender)
        smokerButton = tkinter.Button(frameTopRow, text="By Smoker", command=self.show_smoker)

        ## GRID LAYOUT
        ##############
        frameTopRow.grid(row=0, column=0, columnspan=20, sticky='EW', padx=5, pady=5, ipadx=5, ipady=5)

        frameAbout.grid(row=4, column=0, columnspan=20, padx=5, pady=5)
        aboutLabel.grid(row=0, column=0, columnspan=20, sticky='EW', padx=5, pady=5, ipadx=5, ipady=5)

        openButton.grid(row=0, column=0, sticky='W', padx=5, pady=5)
        plotButton.grid(row=0, column=2, sticky='W', padx=5, pady=2)
        genderButton.grid(row=0, column=3, sticky='W', padx=5, pady=2)
        smokerButton.grid(row=0, column=4, sticky='W', padx=5, pady=2)

        plot_widget = self.canvas.get_tk_widget()
        plot_widget.grid(row=6, column=0, columnspan=20, sticky='EW', padx=5, pady=5, ipadx=5, ipady=5)

    ## OTHER FUNCTIONS
    ##################

    def on_open(self):
        ftypes = [('CSV files', '*.csv'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        if filename != '':
            self.data = pd.read_csv(filename)

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

    def show_plot(self):
        self.ax.scatter(self.data['total_bill'], self.data['tip'], color='black')
        sns.despine()
        self.ax.set_xlabel('Total Bill (£)')
        self.ax.set_ylabel('Tips (£)')
        self.canvas.draw()

    def show_gender(self):
        colors = ['red' if person=='Male' else 'blue' for person in self.data['sex']]
        self.ax.scatter(self.data['total_bill'], self.data['tip'], color=colors)
        sns.despine()
        self.ax.set_xlabel('Total Bill (£)')
        self.ax.set_ylabel('Tip (£)')
        self.canvas.draw()

    def show_smoker(self):
        colors = ['yellow' if smoker=='Yes' else 'black' for smoker in self.data['smoker']]
        self.ax.scatter(self.data['total_bill'], self.data['tip'], color=colors)
        sns.despine()
        self.ax.set_xlabel('Total Bill (£)')
        self.ax.set_ylabel('Tip (£)')
        self.canvas.draw()

if __name__ == "__main__":
    app = InteractiveDemo(None)
    app.title(' Demo ')
    app.mainloop()
