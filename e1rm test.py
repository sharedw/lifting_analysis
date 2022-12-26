# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:46:32 2021

@author: share
"""

import numpy as np

data = np.array([[250,5],[300,1]])

print(data[0])

i = 0
j=0

weight = []
reps = []

while i < len(data):
    weight =np.append(weight,data[i,j]) 
    reps =np.append(reps,data[i,j+1]) 
    i = i + 1
    
e1rm = weight*(36/(37-reps))


