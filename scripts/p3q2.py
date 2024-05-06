import numpy as np
import matplotlib.pyplot as plt

n_values = [2, 3, 5, 10, 20, 50, 100]
m = 100

# Parameters for the exponential distribution with lambda = 2
lambda_exp = 2
mu_exp = 1 / lambda_exp
sigma_exp = 1 / lambda_exp

def generate_samples(n):
    # Generate m samples of size n
    X = np.random.exponential(1/lambda_exp, (m, n))

    # sum each collumn of 2D array X
    S_n = np.sum(X, axis=1)

    # calculate Z_n and Z'_n
    Z_n = (S_n - n * mu_exp) / (np.sqrt(n) * sigma_exp)
    Z_prime_n = (S_n - n * mu_exp) / (n * sigma_exp)
    return Z_n, Z_prime_n


# length of n_values rows, 2 columns to display all histograms
fig, ax = plt.subplots(len(n_values), 2, figsize=(12, 18))

for i, n in enumerate(n_values):
    Z_n, Z_prime_n = generate_samples(n)
    
    # Plot for Z_n
    ax[i, 0].hist(Z_n, bins=10, color='blue', alpha=0.7, density=True)
    ax[i, 0].set_title(f'Histogram of $Z_n$ for n = {n} (Exp Dist)')
    ax[i, 0].set_xlabel('$Z_n$')

    # Plot for Z'_n
    ax[i, 1].hist(Z_prime_n, bins=10, color='green', alpha=0.7, density=True)
    ax[i, 1].set_title(f'Histogram of $Z\'_n$ for n = {n} (Exp Dist)')
    ax[i, 1].set_xlabel('$Z\'_n$')

plt.tight_layout()
plt.savefig('p3q2.png')


