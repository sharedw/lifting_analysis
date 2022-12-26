# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 08:13:37 2022

@author: share
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:13:01 2021

@author: share
"""

#lifting data import

import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import matplotlib.dates

#date formatting
#%m/#%d/%y"

#import data from notes and put it in a list
data = open("liftingpostcovid.txt","r")
rawNotes = [(line.strip()).split() for line in data]
data.close()
        

def masterFunc (liftName):
    

    weight = []
    reps = []
    liftDate = []
    i = 0
    
    
    # print(rawNotes)
    
    #find each instance of the lift
    #make sure its not a variation eg 'cg bench' 'front squat'
    #save weight, reps, and date in an array
    while i < len(rawNotes):
        if liftName in rawNotes[i]:
            if str(rawNotes[i][0]) != liftName:
                i = i + 1
            else:
                # print(rawNotes[i])
                weight = np.append(weight,rawNotes[i][1])
                reps = np.append(reps,rawNotes[i][2])
                j = i
                while j > 0:
                    if "/" in rawNotes[j-1][0]:
                        newDate = datetime.datetime.strptime(rawNotes[j-1][0], '%m/%d/%y')
                        newDate = matplotlib.dates.date2num(newDate)
                        liftDate = np.append(liftDate,newDate)
                        j= 0
                    else: 
                        j = j-1
                
        i= i+1
    

    x = 0
    
    #find the highest e1rm for each day
    highestReps = []
    while x < len(reps):
        if "," in reps[x]:
            newReps = [int(x) for x in reps[x].split(',')]
            highestReps = np.append(highestReps,(max(newReps)))
            
            x = x + 1
        elif "x" in reps[x]:
            newReps = [reps[x][2:len(reps[x])]]
            x = x + 1
            highestReps = np.append(highestReps,newReps)
        else:
            newReps = reps[x]
            x = x + 1
            highestReps = np.append(highestReps,newReps)
    
    
    
    #calculate the estimated 1 rep max based on hardest set of each day
    weight = weight.astype(float) 
    highestReps = highestReps.astype(float)
    p = 0
    while p < len(highestReps):
        if highestReps[p] > 11:
            highestReps[p] = 11
        p = p + 1
    e1rm = weight*(36/(37-highestReps)) #Bryzcki formula
#    e1rm = weight*highestReps**.1 #Lombardi formula
    
    b = 0
    while b < len(liftDate) -1:
        if liftDate[b] == liftDate[(b+1)]:
            if e1rm[b] < e1rm[(b+1)]:
                liftDate = np.delete(liftDate,b)
                e1rm = np.delete(e1rm,b)
            else:
                liftDate = np.delete(liftDate,b+1)
                e1rm = np.delete(e1rm,b+1)
        b = b+1
            
        
                
                
    #plotting stuff
    plt.figure()
    matplotlib.pyplot.plot_date (liftDate,e1rm)
    plt.xlabel('Date')
    plt.ylabel('Estimated '+str(liftName)+'1 Rep Max')
    ax = plt.gca()
    n = 7  # Keeps every 7th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]
    plt.grid(True)
    plt.suptitle(liftName)
    plt.savefig(str(liftName)+' e1RM')

    return

# masterFunc("Bench")
masterFunc("Deadlift")
# masterFunc("Ohp")
# masterFunc("Squat")



