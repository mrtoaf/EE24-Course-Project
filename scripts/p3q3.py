import numpy as np
import matplotlib.pyplot as plt

n_values = [2, 3, 5, 10, 20, 50, 100]
m = 100

# Parameters for the Bernoulli distribution with p = (0.5, 0.2)
p_values = [0.5, 0.2]

def generate_samples(n, p):

    mu_bernoulli = p
    sigma_bernoulli = np.sqrt(p * (1-p))

    # Generate m samples of size n
    X = np.random.binomial(1, p, (m, n))

    # sum each collumn of 2D array X
    S_n = np.sum(X, axis=1)

    # calculate Z_n and Z'_n
    Z_n = (S_n - n * mu_bernoulli) / (np.sqrt(n) * sigma_bernoulli)
    Z_prime_n = (S_n - n * mu_bernoulli) / (n * sigma_bernoulli)
    return Z_n, Z_prime_n


# length of n_values rows, 2 columns to display all histograms
fig, ax = plt.subplots(len(n_values), 4, figsize=(12, 18))

for j, p in enumerate(p_values):
    for i, n in enumerate(n_values):
        Z_n, Z_prime_n = generate_samples(n, p)
        
        # Plot for Z_n
        ax[i, 2*j].hist(Z_n, bins=10, color='blue', alpha=0.7, density=True)
        ax[i, 2*j].set_title(f'Histogram of $Z_n$ for n = {n}, p = {p}')
        ax[i, 2*j].set_xlabel('$Z_n$')

        # Plot for Z'_n
        ax[i, 2*j+1].hist(Z_prime_n, bins=10, color='green', alpha=0.7, density=True)
        ax[i, 2*j+1].set_title(f'Histogram of $Z\'_n$ for n = {n}, p = {p}')
        ax[i, 2*j+1].set_xlabel('$Z\'_n$')

plt.tight_layout()
plt.savefig('p3q3.png')


