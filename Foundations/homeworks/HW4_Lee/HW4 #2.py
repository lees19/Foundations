# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:42:04 2020

@author: lees19
"""
import numpy as np
from matplotlib import pyplot as plt

def calcf(x):
    return (np.sqrt(9*(1-(x**2)/25)), -np.sqrt(9*(1-(x**2)/25)))

def main(): 
    x = np.linspace(-5, 5, 1000)
    y, minusY = calcf(x)
    
    plt.plot(x, y, color = 'orange', linestyle = '--')
    plt.plot(x, minusY, color = 'orange', linestyle = '--')
    plt.grid(color='lightgray', linestyle = '--')
    plt.show()

if __name__ == "__main__": 
    main() 
    