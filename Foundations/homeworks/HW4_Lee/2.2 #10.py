# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:05:20 2020

@author: lees19
"""
#determine whether the dataset supports the stated proportionality model #10

import numpy as np
from pandas import DataFrame
import statsmodels.api as sm

#y is \propto x**2
x = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]) ** 2 #x**2
y = np.array([4., 11., 22., 35., 56., 80., 107., 140., 175., 215.]) #y

df = DataFrame({'x':x, 'y':y})
X=df['x']
Y=df['y']

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
predictions = model.predict(X)
print_model = model.summary() 
print(print_model)