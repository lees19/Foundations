"""
Bird Project Problem in 2.3; pp. 93-94
"""
from pandas import DataFrame
import statsmodels.api as sm
import matplotlib.pyplot as plt
pulse=[1000, 185, 378, 300, 190, 312, 240,193, 65] #Notice the last item book said 60-70
bodyWeight=[20, 300, 341, 658, 1100, 2000, 2300, 8750, 71000] 
plt.plot(bodyWeight, pulse, 'r*')
plt.title('Pulse vs Body Weight: actual data')
#I just plotted the lists;
#you can use this command to plot lists too (not just arrays)
x = list(map(lambda x: x**(-1/3), bodyWeight)) 
#I will explain lambda later- inline function. 
#Why am I raising bodyweight to the -1/3?
# Paper/pencil work was needed based on 2.3

df=DataFrame({"weight^(-1/3)":x, "pulse":pulse})
X=df['weight^(-1/3)']
Y=df['pulse']
#X = sm.add_constant(X) #Not forcing the y-intercept to zero
#See summary in bold from Monday's class in Blackboard.

model = sm.OLS(Y, X).fit() # We need to figure out the slope m for pulse=m*(BW)^(-1/3)

predictions = model.predict(X) #notice we had this line last time 
#- what does it do? How can you find out?

print(model.summary())
fig=plt.figure()
plt.subplot(2,1,1)
plt.ylabel('Pulse')
plt.xlabel('BW^(-1/3)')
plt.title('Pulse vs (Body Weight)^(-1/3): Used OLS to figure out m in pulse=m*(BW)^(-1/3)')
plt.plot(x, predictions, 'r*')

plt.subplot(2,1,2)
plt.plot(bodyWeight,predictions,label='Geometric Similarity Model')
plt.plot(bodyWeight,pulse,label='Actual Data')
plt.ylabel('Pulse (Beats/min)')
plt.xlabel('Body Weight (g)')
plt.title('Pulse vs Body Weight: smaller birds tend to have larger pulses. ')
plt.legend(framealpha=1, frameon=True, loc="best")
fig.tight_layout()
plt.show()
print("\n")
print('The model we obtained was pulse= ' + "{:.2f}".format(model.params[0])+'* (body weight)^(-1/3)')
print("\n")
print('We used geometric similarity logic to figure out the power on body weight and then OLS to get the slope \n')

error=DataFrame({"Weight":bodyWeight, "Percent Error":abs(pulse-predictions)/pulse*100})
print("Percent Errors \n")
print(error)
    
    