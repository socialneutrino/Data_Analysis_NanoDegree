# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 13:29:52 2015

@author: Alex
"""
import matplotlib as mpl 
mpl.use('agg')
import numpy
from pandas import *
import matplotlib.pyplot as plt

dataFrame = read_csv('stroopdata.csv')

x = dataFrame["Congruent"]
y = dataFrame["Incongruent"]

bins = numpy.linspace(0, 40, 80)

plt.hist(x, bins, alpha=0.5, label='Congruent')
plt.hist(y, bins, alpha=0.5, label='Incongruent')
plt.legend(loc='upper right')
plt.show()