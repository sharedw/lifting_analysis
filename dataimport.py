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
import os
#date formatting
#%m/#%d/%y"
path = 'C:/Users/User/Documents/Python stuff/Python stuff/practice'

os.chdir(path)

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

#import data from notes and put it in a list
data = open("liftingpostcovid.txt","r")
rawNotes = [(line.strip()).split() for line in data]
data.close()

k = 0
while k < len(rawNotes):
    if rawNotes[k] == "Front" and rawNotes[k+1] == "Squat":
        rawNotes[k: k+1] = [''.join(rawNotes[k: k+1])]
    k = k+1
        
    

flatNotes = [x for l in rawNotes for x in l]


#initialize benchWeight and benchReps arrays

def masterFunc (liftName):
    

    weight = []
    reps = []
    liftDate = []
    i = 0
    def findDate(j):
        #Finds corresponding date for a particular set
        while j > 0:
            if "/" in flatNotes[j-1]:
                newDate = datetime.datetime.strptime(flatNotes[j-1], '%m/%d/%y')
                newDate = matplotlib.dates.date2num(newDate)
                j= 0
            else: 
                j = j-1
        return newDate
    
    #create 3 arrays, for lift weight, reps performed, and date performed
    while i < len(flatNotes):
        #make sure entry is in valid form
        if liftName in flatNotes[i]:
            if not containsNumber(flatNotes[i+1]) or not containsNumber(flatNotes[i+2]):
                i = i + 2
                print('oops',flatNotes[i],matplotlib.dates.num2date(findDate(i)))
            #add value for rep and weight to list
            else:
                weight = np.append(weight,flatNotes[i+1])
                reps = np.append(reps,flatNotes[i+2])
                j = i
                # add corresponding date value to list
                liftDate = np.append(liftDate, findDate(j))
                
        i= i+1
        
######### do error test and print line for which iti doesnt work and date and stufdf here


    
    #find the hardest set for each day
    x = 0
    
    #grab only value of highest reps performed that day, discard lighter sets
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
            highestReps = np.append(highestReps,newReps)\
            
    weight = weight.astype(float)
    highestReps = highestReps.astype(int)
    # print(highestReps)
    
    #creating empty rep max table
    repidx = [i for i in range(1,11)]
    repweight = [0 for i in range(1,11)]
    table = np.array(list(zip(repidx,repweight)))
    
    
    n = 0
    while n < len(highestReps):
        highestReps[n] = min(highestReps[n],10)
        idx = highestReps[n]-1
        if weight[n] > repweight[idx]:
            repweight[idx] = weight[n]
        n = n + 1
    table = np.array(list(zip(repidx,repweight)))
    
    highestReps = highestReps.astype(int)
    #calculate the estimated 1 rep max based on hardest set of each day
    
#    print(highestReps)
#    print(weight)
    e1rm = weight*(36/(37-highestReps)) #Bryzcki formula
#    e1rm = weight*highestReps**.1 #Lombardi formula
#    print(e1rm)
    
    
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


    fig, ax =plt.subplots(1,1)
    ax.set_title(liftName)
    data=table
    column_labels=['Reps','Weight']
    ax.axis('tight')
    ax.axis('off')
    collWidth = '200'
    ax.table(cellText=data,colLabels=column_labels,loc="center")
     
    return

masterFunc("Bench")
masterFunc("Deadlift")
masterFunc("Ohp")
masterFunc("Squat")



