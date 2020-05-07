# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:28:30 2020

@author: emetz
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DATA_VIS_PROJECT_CSV.csv', index_col='day')
#print(df)

fig, ax1 = plt.subplots()
plt.title('daily_completion vs time spent in department')
ax1.set_ylabel('completion %')
ax1.set_xlabel('day')
days = df.index
completion = df.dailyCPer
ax1.bar(days, completion)

ax2 = ax1.twinx()
ax2.set_ylabel('time in dept')
time = df.deptTime
ax2.plot(days, time, color='orange')
plt.savefig('dailyComp_deptTime.png')

"""
    Is there a noticeable correlation between time spent outside of my
    department and mood?
"""

fig, ax1 = plt.subplots()
plt.title('mood vs time spent outside dept')
ax1.set_ylabel('mood')
days = df.index
mood = df.mood
ax1.bar(days, mood)

ax2 = ax1.twinx()
ax2.set_xlabel('day')
ax2.set_ylabel('time outside department (minutes)')
ax2.plot(df.oTime, color='tab:orange')
plt.savefig('mood_v_otime.png')

mood_counts = df['mood'].value_counts().sort_index()

"""
    Find the occurrences of each mood type.
"""

fig2, ax = plt.subplots()
plt.title('count of days for each mood type')
ax.set_xlabel('mood')
ax.set_ylabel('count of occurrences')
mood = mood_counts.index
count = mood_counts.values
ax.bar(mood, count)
plt.savefig('mood_occurrence.png')

"""
    Compare the amount of time spent each day on daily tasks.
    
    NOTE:  Can't get legend to work.
"""

fig3, ax = plt.subplots()
days = df.index
freight = df.frTime
bins = df.binTime
picks = df.pickTime
downstock = df.dTime
price_changes = df.pcTime
section_work = df.swTime
ax.bar(days, freight)
ax.bar(days, bins)
ax.bar(days, picks)
ax.bar(days, downstock)
ax.bar(days, price_changes)
ax.bar(days, section_work)
plt.title('amount of time spent on daily tasks')
plt.savefig('daily_task_comparison.png')