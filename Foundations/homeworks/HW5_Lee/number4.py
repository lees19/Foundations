# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:12:40 2020

@author: lees19
"""
import numpy as np
from matplotlib import pyplot as plt

def s(s, i, h): 
    return s + h*(-.0015*i*s)
def i(s, i, h): 
    return i + h*(-.65*i +.0015*i*s)
def r(r, i, h): 
    return r + h*(.65 * i)

def main(): 
    N = 2000
    h = .1
    x = np.arange(0, 6+h, h)
    S = np.arange(0., 61)
    I = np.arange(0., 61)
    R = np.arange(0., 61)
    
    I[0] = 6.0
    S[0] = 1994.0
    R[0] = 0.0
    
    print("S \t I \t R")
    print(str(S[0]) + "\t" + str(I[0]) + "\t" + str(R[0]))
    
    for j in range(1, 61): 
        S[j] = s(S[j-1], I[j-1], h)
        I[j] = i(S[j-1], I[j-1], h)
        R[j] = r(R[j-1], I[j-1], h)
        print(str(S[j]) + "\t" + str(I[j]) + "\t" + str(R[j]))
    
    plt.plot(x, S, 'ro')
    plt.plot(x, I, 'bo')
    plt.plot(x, R, 'go')
        
    
if __name__ == "__main__": 
    main() 
    