# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:40:45 2022

@author: User
"""

import numpy as np
def fizzbuzz(n):
    # your code here
    arr = np.array(0)
    i = 0 
    print(type(arr),arr)
    while i < n:
        arr = arr.append(i)
        i = i + 1
    return

fizzbuzz(4)