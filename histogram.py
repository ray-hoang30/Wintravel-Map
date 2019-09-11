# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import matplotlib.pyplot as plt

my_data = numpy.genfromtxt('Time saved2.csv', delimiter=',')

b = my_data[:][1:]
sums = b.sum(axis=0)
c = int(sums[0])
database = b.transpose()[0]
times = b.transpose()[5]
histogram = numpy.empty([1,c])

cnt = 0

for counter in range(len(database)):
    for iterate in range(int(database[counter])):
        histogram[0][cnt] = times[counter]
        cnt += 1

average = numpy.mean(histogram)

plt.hist(times,bins=numpy.linspace(-15, 15, 30), weights=database)
plt.title("Extra Time Needed to Get to New Hospital (compared to old one)")
plt.ylabel("# of People")
plt.xlabel("Extra Time(min)")