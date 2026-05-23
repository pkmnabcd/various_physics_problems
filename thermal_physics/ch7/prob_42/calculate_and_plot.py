import numpy as np
import math
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve, lambdify
import matplotlib.pyplot as plt

"""
This program does the numerical integration for the visible
spectrum energy and plots the spectrum for T=1500 K.
"""


# Constants
class Const:
    # Physical Constants
    k_J = 1.381 * pow(10,-23)      # J / K
    k_eV = 8.617 * pow(10,-5)      # eV / K
    h = 6.626 * pow(10, -34)       # J s
    G = 6.674 * pow(10, -11)       # N m^2 / kg^2
    c = 2.998 * pow(10, 8)         # m / s

    # Other Constants
    m_e = 9.109 * pow(10, -31)     # kg              mass of electron
    m_p = 1.673 * pow(10, -27)     # kg              mass of proton
    avogadro = 6.022 * pow(10, 23) # unitless

    # Math Constants
    pi = math.pi


# Plot the energy spectrum
temp = 1500 # K
h, c, ep, k, T = symbols("h c epsilon, k, T", positive=True)

spectrum = 8 * pi / ((h * c) ** 3)
spectrum *= ep ** 3 / (exp(ep / (k * T)) - 1)
print(f"Energy Spectrum: {spectrum}")

spectrum_prep = spectrum.subs(h, Const.h).subs(c, Const.c).subs(k, Const.k_eV).subs(T, temp)
spectrum_lambda = lambdify(ep, spectrum_prep, "numpy")
energy_array = np.linspace(pow(10, -3), 2.3*pow(10, 0), 10_000)
spectrum_array = spectrum_lambda(energy_array)
plt.plot(energy_array, spectrum_array)
plt.title(f"Planck Spectrum for T={temp} K")
plt.xlabel("Photon Energy (eV)")
plt.ylabel("Energy Density Per Photon Energy (J/(J m^3))")
plt.savefig("energy_vs_spectrum.png")
