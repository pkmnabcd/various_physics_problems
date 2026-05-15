import numpy as np
import matplotlib.pyplot as plt
from math import pow, pi, log

# This program plots entropy of helium-3 at low temperatures as a function of temp.
# It also calculates some properties of helium-3 when modeled as a nearly
# degenerate Fermi gas.

# Constants
k_J = 1.381 * pow(10,-23)      # J / K
k_ev = 8.617 * pow(10,-5)      # eV / K
h = 6.626 * pow(10, -34)       # J s
G = 6.674 * pow(10, -11)       # N m^2 / kg^2
m_e = 9.109 * pow(10, -31)     # kg              mass of electron
m_p = 1.673 * pow(10, -27)     # kg              mass of proton
avogadro = 6.022 * pow(10, 23) # unitless



# Get fermi energy, fermi temp, and heat capacity
n_over_v = 1.62757 * pow(10, 28) # m^-3
he3_mass = 3.016 * pow(10, -3) / avogadro  # molar mass / avogadro's number

fermi_energy = pow(h, 2) / 8 / he3_mass * pow(3/pi * n_over_v, 2/3)
fermi_temp = fermi_energy / k_J
heat_capacity = pow(pi, 2) * k_J / 2 / fermi_energy 

print(f"Helium-3 gas fermi energy: {fermi_energy:e} J.")
print(f"Helium-3 gas fermi temp: {fermi_temp:e} K.")
print(f"Helium-3 gas heat capacity: ({heat_capacity:e} T^-1)NkT.")


T = np.linspace(0, 0.72, 1000)
s_s = np.full(1000, 1 * k_J * log(2))
s_g = heat_capacity * 1 * k_J * T

plt.plot(T, s_s, label="Solid")
plt.plot(T, s_g, label="Degenerate Gas")
plt.title("Helium-3 Solid vs degenerate gas entropy", wrap=True)
plt.xlabel("T (K)")
plt.ylabel("Entropy (J/K)")
plt.legend()
plt.savefig("entropies.png")
