# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:17:59 2015

@author: Alex
"""

from scipy import stats
from pandas import *

dataFrame = read_csv('stroopdata.csv')
x = dataFrame["Congruent"]
y = dataFrame["Incongruent"]

#Calculate t-statistic
scipy.stats.ttest_rel(x, y)