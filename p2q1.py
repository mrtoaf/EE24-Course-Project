import numpy as np
import matplotlib.pyplot as plt

lambda_ = 1.0
samples = 100

# Method analyzed in part (b) of Problem 10
# To simulate exponential random variable with parameter λ

# We generate values u ∈ (0,1) of a uniformly distrivuted random value U
u = np.random.uniform(0, 1, samples)

# And we set X to the value for which 1-e^(-λx) = u, or x = -ln(1-u)/λ
x = -np.log(1 - u) / lambda_

# Plotting
plt.hist(x, bins=10, alpha=0.7, label='Histogram of samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Exponential Distribution Samples')
plt.legend()
plt.show()


