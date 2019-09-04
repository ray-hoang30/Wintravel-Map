# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:09:05 2019

@author: Ray
"""

import numpy
a = numpy.genfromtxt('time saved.csv',delimiter=',')
a = a[1:,:]
print (a)