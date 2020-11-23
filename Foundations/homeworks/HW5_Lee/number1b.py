# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:32:41 2020

@author: lees19
"""
import numpy as np
import matplotlib.pyplot as plt

def main(): 
    first = 0
    last = 100
    n = np.linspace(first, last, last+1)
    P = np.zeros(len(n))
    Q = np.zeros(len(n))
    
    Pnext = lambda P, Q: P-.1*(Q-500)
    Qnext = lambda P, Q: Q+.2*(P-100)
    
    P[0] = 100
    Q[0] = 200
    
    for j in range(1, len(n)): 
        P[j] = Pnext(P[j-1], Q[j-1])
        Q[j] = Qnext(P[j-1], Q[j-1])
        
    print('List for the price: ')
    print(P)
    print('List for the quantity: ') 
    print(Q)
        
if(__name__ == "__main__"): 
    main()
    