# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 12:49:36 2015

@author: Alex
"""

import matplotlib as mpl 
mpl.use('agg')
import matplotlib.pyplot as plt


dataFrame = read_csv('stroopdata.csv')

plotData = [dataFrame["Congruent"], dataFrame["Incongruent"]]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(plotData)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(plotData, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set(facecolor = '#16EAF5', linewidth=2)

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#F62217', linewidth=2)

ax.set_xticklabels(['Congruent', 'Incongruent'])