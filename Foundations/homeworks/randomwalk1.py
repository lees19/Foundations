"""
random walk example
"""
import random
import matplotlib.pyplot as plt

def animate(x,y):
    plt.plot(x,y,'r.')
    return()

def randomwalk(n):
    x=0
    y=0
    #animate(x,y)
    for i in range(n):
        step=random.choice(['N','S','E','W'])
        if step == 'N':
            y+=1
        elif step=='S':
            y+=-1
        elif step=='E':
            x+=1
        else:
            x+=-1
        #animate(x,y)
    return(x,y)

#Finish the main part of the program to answer the question.
        
    