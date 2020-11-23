import matplotlib.pyplot as plt
import numpy as np  
import scipy.integrate as integral
import time

f=lambda y, x: (9-x**2-y**2) 
g=lambda y, x: (2*x**2 + 2*y**2)

#print("integral:", integral.dblquad(f, -2, 2, lambda x: -4, lambda x: 4))

N=1000000
x=np.random.uniform(-np.sqrt(3), np.sqrt(3), N)  
y=np.random.uniform(-np.sqrt(3), np.sqrt(3), N)

z=np.random.uniform(0, 9, N)

hits = np.where( (z<=f(y, x)) & (z >= g(y, x)) )[0].size

volBox = 4*3*9
volume = (hits/N)*volBox
print(volume)
