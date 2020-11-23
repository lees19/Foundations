import numpy as np 
import matplotlib.pyplot as plt

dxdt = lambda x, y: .04*x - .0005*x*y
dydt = lambda x, y: -.2*y + .00049*x*y
h = 25

def eulerRun(xBeg, yBeg, t): 
    N = t.size
    x = np.zeros(N)
    y = np.zeros(N)
    x = [55, 80, 105]
    y[0] = yBeg
    for k in range(1, N): 
        #x[k] = x[k-1]+h*dxdt(x[k-1], y[k-1])
        y[k] = y[k-1]+h*(dydt(x[k-1], y[k-1]) / dxdt(x[k-1], y[k-1]))
        
    return x, y

lastT = 105
t = np.arange(55, lastT+h, h) 
x, y = eulerRun(55, 10, t)
print(x)
print(y)
plt.plot(t, y)