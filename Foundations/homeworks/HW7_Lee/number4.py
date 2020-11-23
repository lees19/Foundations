import numpy as np 
import matplotlib.pyplot as plt

#dxdt = lambda x, y: -x + y
dydt = lambda y: y

def eulerRun(xBeg, yBeg, t): 
    N = t.size
    x = np.zeros(N)
    y = np.zeros(N)
    x = t
    y[0] = yBeg
    error = np.zeros(N-1) 
    for k in range(1, N): 
        #x[k] = x[k-1]+h*dxdt(x[k-1], y[k-1])
        y[k] = y[k-1]+h*dydt(y[k-1])
        error[k-1] = (-y[k] + np.exp(x[k]))/ np.exp(x[k])
        
    return error

h = 1
lastT = 1
t = np.arange(0, lastT+h, h) 
error = eulerRun(0, 1, t)
avgError = np.divide(np.abs(np.sum(error)), np.abs(error.size)) * 100
print('Error for %f, %f%%' %(h, avgError))

h = .5
lastT = 1
t = np.arange(0, lastT+h, h) 
error = eulerRun(0, 1, t)
avgError = np.divide(np.abs(np.sum(error)), np.abs(error.size)) * 100
print('Error for %f, %f%%' %(h, avgError))

h = .25
lastT = 1
t = np.arange(0, lastT+h, h) 
error = eulerRun(0, 1, t)
avgError = np.divide(np.abs(np.sum(error)), np.abs(error.size)) * 100
print('Error for %f, %f%%' %(h, avgError))

h = .125
lastT = 1
t = np.arange(0, lastT+h, h) 
error = eulerRun(0, 1, t)
avgError = np.divide(np.abs(np.sum(error)), np.abs(error.size)) * 100
print('Error for %f, %f%%' %(h, avgError))