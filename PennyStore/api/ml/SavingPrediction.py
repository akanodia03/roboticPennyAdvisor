import matplotlib.pyplot as plt
from pandas import read_csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as pltp
import math
from sklearn.linear_model import LinearRegression


# Load data
data_path = os.path.join(os.getcwd(), "SavingPrediction.csv")
dataset = read_csv(data_path, delim_whitespace=True)

# We have 30 entries in our dataset and four features. The first feature is the ID of the entry.
# The second feature is always 1. The third feature is the age and the last feature is the blood pressure.
# We will now drop the ID and One feature for now, as this is not important.
dataset = dataset.drop(['ID', 'One'], axis=1)

# And we will display this graph
#%matplotlib inline
dataset.plot.scatter(x='AccountType', y='PercentageSaving')

# Now, we will assume that we already know the hypothesis and it looks like a straight line
h = lambda x: 5 + 1.24 * x

# Let's add this line on the chart now
accounts = range(1, 85)
estimated = []

for i in accounts:
    estimated.append(h(i))
print("test",estimated)
plt.plot(accounts, estimated, 'b')
#plt.show()
h = lambda x, theta_0, theta_1: theta_0 + theta_1 * x

def cost(X, y, t0, t1):
    m = len(X) # the number of the training samples
    c = np.power(np.subtract(h(X, t0, t1), y), 2)
    return (1 / (2 * m)) * sum(c)

X = dataset.values[:, 0]
y = dataset.values[:, 1]
print('J(Theta) = %2.2f' % cost(X, y, 84, 1.24))

fig = pltp.figure()

# Generate the data
theta_1 = np.arange(-10, 14, 0.1)

J_cost = []
for t1 in theta_1:
    J_cost += [ cost(X, y, 0, t1) ]

pltp.plot(theta_1, J_cost)

pltp.xlabel(r'$\theta_1$')
pltp.ylabel(r'$J(\theta)$')

pltp.show()

cur_x = 2.5 # The algorithm starts at point x
gamma = 0.005 # Step size multiplier
precision = 0.00001
previous_step_size = cur_x

df = lambda x: 2 * x * math.cos(x)

# Remember the learning curve and plot it

while previous_step_size > precision:
    prev_x = cur_x
    cur_x += -gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)

print("The local minimum occurs at %f" % cur_x)

X = dataset[['AccountType']]
y = dataset[['PercentageSaving']]

regr = LinearRegression()
regr.fit(X, y)

# Plot outputs
plt.xlabel('AccountType')
plt.ylabel('Percentage Saving')

plt.scatter(X, y,  color='black')
plt.plot(X, regr.predict(X), color='blue')

plt.show()
plt.gcf().clear()

print( 'Predicted discount at suffire Card   = ', regr.predict(39) )
print( 'Predicted discount at freedom card   = ', regr.predict(45) )
print( 'Predicted discount at Amezon Great Indian Sale   = ', regr.predict(47) )