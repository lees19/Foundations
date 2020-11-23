# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:22:28 2020

@author: lees19
"""
import numpy as np 
import matplotlib.pyplot as plt

def f(x, y): 
    return 4*x - x*y - 2*x**2

def g(x, y): 
    return 2*y - x*y - 3*y**2

def k1(x, y, h): 
    return f(x, y) * h

def l1(x, y, h): 
    return g(x, y) * h

def k2(x, y, h): 
    return f(x + k1(x, y, h)/2, y + l1(x, y, h)/2) * h

def l2(x, y, h): 
    return g(x + k1(x, y, h)/2, y + l1(x, y, h)/2) * h

def k3(x, y, h): 
    return f(x + k2(x, y, h)/2, y + l2(x, y, h)/2) * h

def l3(x, y, h): 
    return g(x + k2(x, y, h)/2, y + l2(x, y, h)/2) * h

def k4(x, y, h): 
    return f(x+k3(x, y, h), y+k3(x, y, h)) * h

def l4(x, y, h): 
    return g(x+k3(x, y, h), y+k3(x, y, h)) * h

h = .1 
x = np.arange(0, 8+h, h)
y = np.arange(0, 8+h, h)

#initial value = 3
x[0] = .01
y[0] = .1

for i in range(1, x.size): 
    x[i] = x[i-1] + (k1(x[i-1], y[i-1], h) + 2*k2(x[i-1], y[i-1], h)  + 2*k3(x[i-1], y[i-1], h)  + k4(x[i-1], y[i-1], h) )/6
    y[i] = y[i-1] + (l1(x[i-1], y[i-1], h) + 2*l2(x[i-1], y[i-1], h)  + 2*l3(x[i-1], y[i-1], h)  + l4(x[i-1], y[i-1], h) )/6
plt.plot(x, y, label="x(0)=" + str(x[0]) + ", y(0)=" + str(y[0]))
plt.legend(bbox_to_anchor = (1.01, 1), loc='upper left')

x[0] = 2
y[0] = 1

for i in range(1, x.size): 
    x[i] = x[i-1] + (k1(x[i-1], y[i-1], h) + 2*k2(x[i-1], y[i-1], h)  + 2*k3(x[i-1], y[i-1], h)  + k4(x[i-1], y[i-1], h) )/6
    y[i] = y[i-1] + (l1(x[i-1], y[i-1], h) + 2*l2(x[i-1], y[i-1], h)  + 2*l3(x[i-1], y[i-1], h)  + l4(x[i-1], y[i-1], h) )/6
plt.plot(x, y, label="x(0)=" + str(x[0]) + ", y(0)=" + str(y[0]))
plt.legend(bbox_to_anchor = (1.01, 1), loc='upper left')

x[0] = .5
y[0] = 2

for i in range(1, x.size): 
    x[i] = x[i-1] + (k1(x[i-1], y[i-1], h) + 2*k2(x[i-1], y[i-1], h)  + 2*k3(x[i-1], y[i-1], h)  + k4(x[i-1], y[i-1], h) )/6
    y[i] = y[i-1] + (l1(x[i-1], y[i-1], h) + 2*l2(x[i-1], y[i-1], h)  + 2*l3(x[i-1], y[i-1], h)  + l4(x[i-1], y[i-1], h) )/6
plt.plot(x, y, label="x(0)=" + str(x[0]) + ", y(0)=" + str(y[0]))
plt.legend(bbox_to_anchor = (1.01, 1), loc='upper left')

