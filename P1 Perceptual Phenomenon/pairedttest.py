# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 21:17:59 2015

@author: Alex
"""
import scipy
import pandas
from scipy import stats
from pandas import *

dataFrame = read_csv('stroopdata.csv')
x = dataFrame["Congruent"]
y = dataFrame["Incongruent"]

#Calculate t-statistic
print scipy.stats.ttest_rel(x, y)
print 't-statistic = %6.3f pvalue = %s' %  scipy.stats.ttest_rel(x, y)