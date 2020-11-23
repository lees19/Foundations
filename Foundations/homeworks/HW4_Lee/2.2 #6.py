# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:47:56 2020

@author: lees19
"""
import numpy as np
from pandas import DataFrame
import statsmodels.api as sm

#y is \propto sqrt(z)
y = np.array([3.5, 5, 6, 7, 8]) #y
z = np.array(np.sqrt([3., 6., 9., 12., 15.])) #sqrt(z)

df = DataFrame({"y": y, "z^1/2":z})
Y=df['y']
Z=df['z^1/2']

#Y = sm.add_constant(Y)

model = sm.OLS(Z, Y).fit()
predictions = model.predict(Y)
print_model = model.summary() 
print(print_model) 