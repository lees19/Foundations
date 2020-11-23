# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:29:45 2020

@author: lees19
"""

from pandas import DataFrame
import statsmodels.api as sm
import matplotlib.pyplot as plt
pulse=[660, 670, 420, 300, 205, 120, 85, 70, 72, 38, 40, 48] #Notice the last item book said 60-70
bodyWeight=[4, 25, 200, 300, 2000, 5000, 30000, 50000, 70000, 450000, 500000, 3000000] 
plt.plot(bodyWeight, pulse, 'r*')
plt.title('Pulse vs Body Weight: actual data')

x = list(map(lambda x: x**(-1/3), bodyWeight)) 

df=DataFrame({"weight^(-1/3)":x, "pulse":pulse})
X=df['weight^(-1/3)']
Y=df['pulse']

#X = sm.add_constant(X)
model = sm.OLS(Y, X).fit() 

predictions = model.predict(X)

print(model.summary())

error=DataFrame({"Weight":bodyWeight, "Percent Error":abs(pulse-predictions)/pulse*100})
print("Percent Errors \n")
print(error)
