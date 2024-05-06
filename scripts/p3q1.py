import numpy as np
import matplotlib.pyplot as plt

n_values = [2, 3, 5, 10, 20, 50, 100]
m = 100

# Mean (μ) and variance (σ^2) for U(0,1)
mu = 0.5
var = 1/12
sigma = np.sqrt(var)

def generate_samples(n):
    # Generate m samples of size n
    X = np.random.uniform(0, 1, (m, n))

    # sum each collumn of 2D array X
    S_n = np.sum(X, axis=1)

    # calculate Z_n and Z'_n
    Z_n = (S_n - n * mu) / (np.sqrt(n) * sigma)
    Z_prime_n = (S_n - n * mu) / (n * sigma)
    return Z_n, Z_prime_n


# length of n_values rows, 2 columns to display all histograms
fig, ax = plt.subplots(len(n_values), 2, figsize=(12, 18))

for i, n in enumerate(n_values):
    Z_n, Z_prime_n = generate_samples(n)
    
    # Plot for Z_n
    ax[i, 0].hist(Z_n, bins=10, color='blue', alpha=0.7, density=True)
    ax[i, 0].set_title(f'Histogram of $Z_n$ for n = {n}')
    ax[i, 0].set_xlabel('$Z_n$')

    # Plot for Z'_n
    ax[i, 1].hist(Z_prime_n, bins=10, color='green', alpha=0.7, density=True)
    ax[i, 1].set_title(f'Histogram of $Z\'_n$ for n = {n}')
    ax[i, 1].set_xlabel('$Z\'_n$')

plt.tight_layout()
plt.savefig('p3q1.png')