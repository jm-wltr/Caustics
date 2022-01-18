#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:26:11 2022

@author: Jaimew
"""

import numpy as np
from numpy import sin
from numpy import cos
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal")

num = 1000
x = np.zeros(num)
y = np.zeros(num)
i = 0
c = 1
for t in np.linspace(0,2*np.pi,num):
    x[i] = cos(t)
    y[i] = sin(t) + 1
    i = i + 1
    
num = 10
i = 0
c = 1
for t in np.linspace(0,2*np.pi,num):
    ax.plot([cos(t), 0], [sin(t)+1, 0], color = "lightgray", linewidth = 0.3)
    ax.plot([cos(t), (1+c)*cos(t) - 2*c*cos(t)], \
            [sin(t), (1+c)*sin(t) - 2*c*sin(t)])

ax.plot(x,y)
