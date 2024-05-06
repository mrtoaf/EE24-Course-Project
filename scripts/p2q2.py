import numpy as np
import matplotlib.pyplot as plt

samples = 100

# ui^(1) and ui^(2) are independent samples from 
# the Unif([0,1]) distribution
u1 = np.random.uniform(0, 1, samples)
u2 = np.random.uniform(0, 1, samples)

# Definition of variable X
x = np.sqrt(2*np.log(1/u1) * np.cos(2*np.pi*u2))

# Plotting
plt.hist(x, bins=20, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Variable X')
plt.savefig('p2q2.png')

