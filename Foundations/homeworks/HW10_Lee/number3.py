import matplotlib.pyplot as plt
import numpy as np  
import scipy.integrate as integral
import time

f=lambda x: (6-x) - x**2

#print("integral:", integral.dblquad(f, -2, 2, lambda x: -4, lambda x: 4))

N=1000000
x=np.random.uniform(0, 2, N)  
y=np.random.uniform(0, 6, N)

hits = np.where(y<=f(x))[0].size

#around seven positive y/x axis
volBox = 2*6
volume = (hits/N)*volBox
print(volume)