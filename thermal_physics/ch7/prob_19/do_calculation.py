from math import pow, exp, pi

# This program acts as my calculator for some calculations for this problem.
AVOGADRO = 6.022 * pow(10, 23)
PLANCK = 6.626 * pow(10, -34)
ELECTRON_M = 9.1094 * pow(10, -31)
BOLTZMANN = 1.381 * pow(10, -23) # in J/K

# Get the fraction N/V
n_over_v = AVOGADRO * 8960 / 0.063546
print(f"N/V = {n_over_v} electrons / m^3")

# Get Fermi Energy
e_f = pow(PLANCK, 2) / (8 * ELECTRON_M) * pow(3 / pi * n_over_v, 2/3)
print(f"Fermi Energy = {e_f} J")

# Get Fermi Temp
t_f = e_f / BOLTZMANN
print(f"Fermi Temp = {t_f} K")

# Get Degenerate Pressure
p = 2/5 * e_f * n_over_v
print(f"Degenerate Pressure = {p} Pa")

# Get Bulk Modulus
b = 5/3 * p
print(f"Degenerate Pressure = {b} Pa")
