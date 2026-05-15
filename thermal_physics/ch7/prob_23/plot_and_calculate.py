import numpy as np
import matplotlib.pyplot as plt
from math import pow, pi

# This program plots the total energy of a white dwarf as a function of R
# and calculates some fermi gas properties of the sun's white dwarf state.
# It also does some calculations to find the mass where relativistic effects
# dominate.

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
k = 1.381 * pow(10,-23) # in J/K

density = M / (4/3*pi*pow(R, 3))

fermi_energy = pow(9, 2/3) * pow(M, 2/3) * pow(h, 2) / ( 32 * pow(pi, 4/3) * m_e * pow(m_p, 2/3) * pow(R, 2) )
fermi_temp = fermi_energy / k

print(f"The Sun's white dwarf radius: {R:e} m")
print(f"The Sun's white dwarf density: {density:e} kg/m^3")
print(f"The Sun's Fermi energy: {fermi_energy:e} J")
print(f"The Sun's Fermi temperature: {fermi_temp:e} K")
print()


# Now calculate M such that average energy equals m_ec^2
c = 2.998 * pow(10, 8)
rest_energy = m_e * pow(c, 2)

alpha = 3/5 * pow(9, 2/3) / (32 * pow(pi, 4/3)) * pow(G, 2) * m_e * pow(m_p, 8/3) / pow(h, 2) / pow(0.0294, 2)
m = pow(rest_energy / alpha, 3/4)
print(f"The mass needed before relativistic effects take over is {m:e} kg.")
