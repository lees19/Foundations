import random 
import matplotlib.pyplot as plt 
import numpy as np

def animate(x, y): 
    plt.plot(x, y, 'r.')
    return()

def randomwalk(n): 
    (x, y) = (0, 0)
    
    for i in range(n): 
        (dx, dy) = random.choice([(0,1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
        
    return (x, y)
        
N = 10000
notransit = 0
transitPercent = np.zeros(50)

for j in range(50): 
    notransit = 0
    
    for i in range(N): 
        pt = randomwalk(j)
        dist = abs(pt[0])+abs(pt[1])
        if dist <= 5: 
            notransit += 1
        
    transitPercent[j] = notransit/N
    

print(np.where(transitPercent >= .5))
