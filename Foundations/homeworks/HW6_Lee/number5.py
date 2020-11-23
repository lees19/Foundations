# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:10:39 2020

@author: lees19
"""

import numpy as np
import matplotlib.pyplot as plt

def pPrime(p): 
    return .24*p*(11-p)

h = .1 
#x = np.arange(-10-h, 21+h, h)
x = np.arange(0, 40+h, h)
P = np.zeros_like(x)
dP = np.zeros_like(x)

#initial value = 3
P[0] = -2

for i in range(1, x.size): 
    dP[i-1] = pPrime(P[i-1])
    P[i] = P[i-1] + h*(pPrime(P[i-1]))

print(P)

plt.plot(P)
plt.plot(np.ones_like(P)*11)
plt.plot(np.zeros_like(P))

