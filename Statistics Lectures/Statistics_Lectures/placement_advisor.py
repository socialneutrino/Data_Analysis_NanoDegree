# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 14:05:34 2015

@author: Alex
"""

from pandas import *
geyser = read_csv('Faithful Geyser Eruptions - Sheet1.csv')
print "Measures of central tendency:"
print geyser["Eruption Duration"].mean()
print geyser["Eruption Duration"].median()
print geyser["Eruption Duration"].mode()

print "Measures of variance: pop var and sample var"
print geyser["Eruption Duration"].pvariance()
print geyser["Eruption Duration"].var()