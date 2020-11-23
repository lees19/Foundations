import numpy as np 
import matplotlib.pyplot as plt

dxdt = lambda x, y: -x + y
dydt = lambda x, y: -x - y
h = .1

def eulerRun(xBeg, yBeg, t): 
    N = t.size
    x = np.zeros(N)
    y = np.zeros(N)
    x[0] = xBeg
    y[0] = yBeg
    for k in range(1, N): 
        x[k] = x[k-1]+h*dxdt(x[k-1], y[k-1])
        y[k] = y[k-1]+h*dydt(x[k-1], y[k-1])
        
    return (x, y)

lastT = 10
t = np.arange(0, lastT+h, h) 
x, y = eulerRun(1, 0, t)
plt.plot(t, a)
plt.plot(t, b)

