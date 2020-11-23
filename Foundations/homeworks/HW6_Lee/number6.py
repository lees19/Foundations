# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:22:28 2020

@author: lees19
"""
import numpy as np 
import matplotlib.pyplot as plt

#this is also dP/dt
def g(p): 
    return .24*p*(11-p)

def k1(p, h): 
    return g(p) * h

def k2(p, h): 
    return g(p + (k1(p, h)/2))* h 

def k3(p, h): 
    return g(p + (k2(p, h)/2))* h 

def k4(p, h): 
    return g(p+k3(p, h))* h

h = .1 
x = np.arange(0, 8+h, h)
P = np.zeros_like(x)
dP = np.zeros_like(x)

#initial value = 3
P[0] = 3

for i in range(1, x.size): 
    #dP[i-1] = g(P[i-1])
    P[i] = P[i-1] + ((k1(P[i-1], h) + 2*k2(P[i-1], h) + 2*k3(P[i-1], h) + k4(P[i-1], h))/6)
    
#print P(2) 
print(P[20])

plt.plot(P)
