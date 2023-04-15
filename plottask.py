# plottask.py 
# Weekly Task 8
'''
Description from Andrew: 
Write a program called plottask.py that displays:
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc)
'''
# reources used: 
# https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/
# https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o
# https://www.geeksforgeeks.org/matplotlib-pyplot-twinx-in-python/
# https://stackoverflow.com/questions/21226868/superscript-in-python-plots
# Author: Shane Keenan 
# status: complete

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
# create random data for the normal distribution to be plotted in histogram
normData = np.random.normal(loc = 5, scale = 2, size = 1000)
# create h(x) = x^3 function data - np.array(range(0,10)) only outputs 10 points - 
x = np.array(range(0,10))
y = x**3
'''
# plot the histogram  - syntax -  https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/
plt.figure(0)
plt.hist(normData, bins=60, density=True)
plt.show()
'''
# instead plot using object-orientated matplotlib 
# - to plot two axes together - https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o
fig, ax1 = plt.subplots()
ax1.hist(normData, bins=60, density=True, color='blue')
# Add axis labels to histogram 
ax1.set_xlabel('Number')
ax1.set_ylabel('Frequency')
#  make and return a second axis ax2 that shares the x-axis with ax1 . https://www.geeksforgeeks.org/matplotlib-pyplot-twinx-in-python/
ax2 = ax1.twinx()
# plot lineplot on second axis 
ax2.plot(x, y, color = 'red', linewidth=2, label='$h(x)=x^3$')
# add legend and title 
# how to superscritp the power - https://stackoverflow.com/questions/21226868/superscript-in-python-plots
ax2.legend(loc='upper left')
plt.title('Normal distribution (mean = 5, SD = 2) and plot function $h(x)=x^3$')
#plt.show()
plt.savefig('hist_func_plot.png')