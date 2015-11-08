# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 12:20:38 2015

@author: Alex
"""

import plotly.plotly as py
import plotly.graph_objs as go
from pandas import *
dataFrame = read_csv('stroopdata.csv')
import numpy as np

y0 = dataFrame["Congruent"]
y1 = dataFrame["Incongruent"]

congruent = go.Box(
    y=y0
)
incongruent = go.Box(
    y=y1
)
data = [congruent, incongruent]
plot_url = py.plot(data, filename='basic-box-plot')