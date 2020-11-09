#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Part 1-1
#Code for showing the amount of fruit my wife and I eat every week

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Apples', 'Pears', 'Oranges', 'Grapes', 'Bananas']
matt_num = [5, 4, 5, 40, 2]
jazz_num = [0, 3, 2, 58, 2]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, matt_num, width, label='Matt')
rects2 = ax.bar(x + width/2, jazz_num, width, label='Jazz')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count')
ax.set_title('Fruit eaten per week')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


# In[28]:


#Part 1-2
#A breakdown of the hours in my day
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Sleeping', 'Working', 'Homework', 'Recreation'
sizes = [7, 5, 5, 7]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[ ]:




