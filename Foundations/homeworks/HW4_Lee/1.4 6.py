# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:41:26 2020

@author: lees19
"""
from matplotlib import pyplot as plt
import numpy as np

def calcP(p, q): 
    return p - .1*(q - 500)

def calcQ(p, q): 
    return q + .2*(p-100)

def main(): 
    L = 60
    n = np.arange(0, L+1)
    
    P = np.zeros(len(n))
    Q = np.zeros(len(n))
    
    P[0] = 100 
    Q[0] = 500
    
    for i in np.arange(1, L+1): 
        P[i] = calcP(P[i-1], Q[i-1])
        Q[i] = calcQ(P[i-1], Q[i-1])
        
    #plt.plot(n, P, 'ro') # n vs P
    #plt.plot(n, Q, 'bo') # n vs Q
    plt.plot(P, Q, 'go') #P vs Q
    plt.title('P vs Q')
    plt.xlabel('weeks')
    plt.ylabel('Price/Quantity')
    plt.legend(loc = 'center left')
    plt.show()
    
if(__name__ == "__main__"): 
    main()