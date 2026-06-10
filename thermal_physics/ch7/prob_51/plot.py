import numpy as np
import math
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve, lambdify
import matplotlib.pyplot as plt

"""
This program plots the planck spectrum for T=3000 K.
"""


# Constants
class Const:
    # Physical Constants
    k_J = 1.381e-23     # J / K
    k_eV = 8.617e-5     # eV / K
    h = 6.626e-34       # J s
    h_eV = 4.136e-15    # eV s
    G = 6.674e-11       # N m^2 / kg^2
    c = 2.998e8         # m / s

    # Other Constants
    m_e = 9.109e-31     # kg              mass of electron
    m_p = 1.673e-27     # kg              mass of proton
    avogadro = 6.022e23 # unitless

    # Math Constants
    pi = math.pi


# Plot the energy spectrum
temp = 3000 # K
lambda_start = 400 * pow(10, -9)
lambda_end = 700 * pow(10, -9)
h, c, ep, k, T = symbols("h c epsilon, k, T", positive=True)

spectrum = 8 * pi / ((h * c) ** 3)
spectrum *= ep ** 3 / (exp(ep / (k * T)) - 1)
print(f"Energy Spectrum: {spectrum}")

spectrum_prep = spectrum.subs(h, Const.h_eV).subs(c, Const.c).subs(k, Const.k_eV).subs(T, temp)
spectrum_lambda = lambdify(ep, spectrum_prep, "numpy")
energy_array = np.linspace(pow(10, -3), 4.0*pow(10, 0), 10_000)
spectrum_array = spectrum_lambda(energy_array)
visible_region = np.linspace(Const.h_eV*Const.c/lambda_end, Const.h_eV*Const.c/lambda_start, 700)
plt.plot(energy_array, spectrum_array)
plt.fill_between(visible_region, spectrum_lambda(visible_region), color="orange", alpha=0.5)
plt.title(f"Planck Spectrum for T={temp} K")
plt.xlabel("Photon Energy (eV)")
plt.ylabel("Energy Density Per Photon Energy (eV/(eV m^3))")
plt.savefig("energy_vs_spectrum.png")
