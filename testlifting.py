# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 07:48:12 2022

@author: User
"""

import numpy as np
import math 
repidx = [i for i in range(1,11)]
repweight = [0 for i in range(1,11)]

highestReps = [1,3,7,5,3]
weight = [100,200,300,400,500]
k = 0
while k <  len(weight):
    print(k)
    weight[k] = min(weight[k],250)
    k = k + 1

n = 0
while n < len(highestReps):
    idx = highestReps[n]-1
    if weight[n] > repweight[idx]:
        repweight[idx] = weight[n]
    n = n + 1

table = np.array(list(zip(repidx,repweight)))
print(table)

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False