"""
monte carlo method is used to model something which is hard to solve by using probability. 

"""

import matplotlib.pyplot as plt
import numpy as np  
import scipy.integrate as integral
import time

f=lambda y, x: 25 - x**2 - y**2

t0 = time.time()
N=10000
x=np.random.uniform(-5, 5, N)  
y=np.random.uniform(-5, 5, N)
z=np.random.uniform(0, 25, N)

hits = np.where(z<=f(y, x))[0].size

volBox = 25*10*10
volume = (hits/N)*volBox
t1=time.time()

print("Volume using vectorized code: ", volume)
print("The vectorized code method took ", t1-t0 ," time units")

#for loop
t0 = time.time()

counter = 0
for i in range(N): 
    x=np.random.uniform(-5, 5, 1)  
    y=np.random.uniform(-5, 5, 1)
    z=np.random.uniform(0, 25, 1)
    temp = f(y, x)
    if z <= temp: 
        counter += 1
        
forVolume = volBox*counter/N

t1 = time.time()
print("Volume using for loop code: ", forVolume)
print("The for loop code method took ", t1-t0 ," time units")
