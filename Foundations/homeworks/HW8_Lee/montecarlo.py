"""
monte carlo method is used to model something which is hard to solve by using probability. 

"""

import matplotlib.pyplot as plt
import numpy as np  
import scipy.integrate as integral
import time

f=lambda y, x: np.sqrt(9 - (9/4)*x**2 - (9/16)*y**2)

#print("integral:", integral.dblquad(f, -2, 2, lambda x: -4, lambda x: 4))

t0 = time.time()
N=1000000
x=np.random.uniform(-2, 2, N)  
y=np.random.uniform(-4, 4, N)
z=np.random.uniform(0, 3, N)

hits = np.where(z<=f(y, x))[0].size

volBox = (4*8*3)
volume = (2*hits/N)*(4*8*3)
print(volume)

"""
#vectorized

hits = np.where(x**2/4+y**2/16+z**2/9 <= 1)[0].size

"""
