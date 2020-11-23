import matplotlib.pyplot as plt
import numpy as np  
import random 
from scipy import integrate

f = lambda x: 4*x

N=1000
#x = np.linspace(0, 3, N)
x1 = np.random.uniform(0, 2, N)
y = np.random.uniform(0, 1, N)

plt.plot(x1, f(x1)) #a

avg = f(x1).mean() #b #f(x1).mean()
print("average ", avg)


print("integral ", integrate.quad(f, 0, 2)[0]/2) #c 

"""
#box 3 x 1, #d
hits = np.where(y<=f(x1))[0].size
areaBox = (3)
area = (hits/N)*areaBox
print("area ", area)

"""