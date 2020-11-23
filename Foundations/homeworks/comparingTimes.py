"""
Nov. 9, 2020
"""
#code adapted from video from Nov. 4. 
import numpy as np  
import time #New on Nov. 9
N=1000000 #I increased N for Nov 9 
f=lambda x:15*np.sqrt(1-x**2/100) 
t0=time.time() #start time
x=np.random.uniform(-10, 10, N)  
y=np.random.uniform(0, 15, N) 
hits=len(np.where(y<=f(x))[0])
areaofBox=20*15
print("Area is ", 2*hits/N*areaofBox)
t1=time.time() #finish time
print("The vectorized code method took ", t1-t0 ," time units")


#Method 2- using a loop and the same value of Ns
