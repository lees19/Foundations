# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:53:31 2020

@author: lees19
"""


import numpy as np
import matplotlib.pyplot as plt

pArr = np.array([3])
h = .1
diffP = lambda x: .24*x*(11-x)

for i in np.arange(1, 61): 
    pArr = np.append(pArr, pArr[i-1] + h*diffP(pArr[i-1]))
    
print('approximation of P(2): %f' % (pArr[20]))
print('approximation of P(6): %f' % (pArr[60]))

plt.plot(pArr, 'ro')
plt.xlabel('t')
plt.ylabel('P (in hundreds)')
plt.title('Euler Approximation')