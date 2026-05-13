import numpy as np
import matplotlib.pyplot as plt
from math import pow, pi

# This program plots the average number of particles present at an energy state
# as a function of the difference between the energy of the state epsilon and 
# the chemical potential mu.

# Boltzman's const in eV / K
k = 8.617 * pow(10,-5)
h = 6.626 * pow(10, -34)
G = 6.674 * pow(10, -11)
m_e = 9.109 * pow(10, -31)
m_p = 1.673 * pow(10, -27)

# Arbitrary total mass M in kg
M = pow(10, 5)

# R in m
var_R = np.linspace(0, 1_000_000, 1000+1)[1:] # Don't include 0

# Calculate total energy
u_grav = -3/5 * G * pow(M, 2) / var_R
u_kinetic = 0.00882 * pow(M, 5/3) * pow(h, 2) / m_e / pow(m_p, 5/3) / np.power(var_R, 2)
u_total = u_grav + u_kinetic

plt.plot(var_R, u_total)
plt.title("Total Energy with varying R", wrap=True)
plt.xlabel("R (m)")
plt.ylabel("Total Energy (J)")
plt.ylim(0, 1_000_000)
plt.savefig("R_vs_Utotal.png")



# Now do the calculation for the Sun's white dwarf radius.
M = 2 * pow(10, 30) # kg
R = 0.0294 * pow(h, 2) / G / m_e / pow(m_p, 5/3) / pow(M, 1/3)
density = M / (4/3*pi*pow(R, 3))
print(f"The Sun's white dwarf radius: {R:e} m")
print(f"The Sun's white dwarf density: {density:e} kg/m^3")
