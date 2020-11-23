import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice 
import pandas as pd

#fill in the rest.
N = 10000

#A = 0, B = 1, C = 2
faces = np.arange(0, 3)
weights1 = np.array([.65, .1, .25])

a = np.ones(3)
cArr = np.zeros(N)

for i in range(N): 
    counter = 0
    
    while a.any(): 
        roll = np.random.choice(faces, 1, p=weights1)
        if roll == 0: 
            a[0] = 0
        if roll == 1:
            a[1] = 0
        if roll == 2: 
            a[2] = 0
        counter += 1
        
    cArr[i] = counter
    a = np.ones(3)
    
print(cArr.mean())
    
