import numpy as np
import matplotlib.pyplot as plt
from math import pow

# This program plots the average number of particles present at an energy state
# as a function of the difference between the energy of the state epsilon and 
# the chemical potential mu.

# Boltzman's const in eV / K
k = 8.617 * pow(10,-5)

# epsilon-mu in eV
delta = np.linspace(-0.20, 0.20, 1000)
temps = np.array([10, 30, 100, 300, 500, 1000, 2000]) # Temperatures in K

for temp in temps:
    x = delta / (k * temp)
    e_to_x = np.exp(x)
    e_to_neg_x = np.exp(-1*x)
    n = (1/(e_to_x+1+e_to_neg_x)) + (2/(np.pow(e_to_x, 2)+e_to_x+1))
    plt.plot(delta, n, label=f"{temp} K")

plt.title("New particle distribution function", wrap=True)
plt.xlabel("epsilon-mu (eV)")
plt.ylabel("Occupancy")
plt.legend()
plt.savefig("energy_vs_occupancy.png")
