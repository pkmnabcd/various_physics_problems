import numpy as np
import math
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve, lambdify
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
This program does the numerical integration of the blackbody spectrum at
various temperatures, starting with T=3000 K, where we get the fraction
of energy density coming from visible spectrum photons. Later, we
integrate over visible spectrum energies and find the most efficient
temperature for getting visible light from a blackbody.
"""


def getSpectrumVisibleEnergy(spectrum, temp, T, ep):
    """
    spectrum is the sympy expression with everything but T and ep plugged in.
    temp is the current temperature used.
    T is the sympy variable for temperature.
    ep is the sympy variable for energy (epsilon).
    """
    # Visible spectrum wavelengths and energies
    lambda_low = 400 * pow(10, -9)
    lambda_high = 700 * pow(10, -9)
    energy_low = Const.h_eV * Const.c / lambda_high
    energy_high = Const.h_eV * Const.c / lambda_low

    spectrum_prep = spectrum.subs(T, temp)
    spectrum_lambda = lambdify(ep, spectrum_prep, "numpy")
    result, error = quad(spectrum_lambda, energy_low, energy_high)
    return result


def getVisibleEnergyFraction(temp, spectrum, T, ep):
    visible_energy = getSpectrumVisibleEnergy(spectrum, temp, T, ep)
    total_energy = 8 * (Const.pi ** 5) * (Const.k_eV*temp) ** 4 / (15 * (Const.h_eV*Const.c) ** 3)
    fraction = visible_energy / total_energy
    return fraction


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


# Prep the spectrum object that will be used throughout
h, c, ep, k, T = symbols("h c epsilon, k, T", positive=True)
spectrum = 8 * pi / ((h * c) ** 3)
spectrum *= ep ** 3 / (exp(ep / (k * T)) - 1)
print(f"Energy Spectrum: {spectrum}")
spectrum_prep = spectrum.subs(h, Const.h_eV).subs(c, Const.c).subs(k, Const.k_eV)

# Calculate fraction of visible light energy at T=3000 K
temp = 3000 # K
fraction = getVisibleEnergyFraction(temp, spectrum_prep, T, ep)
print(f"For T={temp}, the visible fraction of energy is {fraction:.4f}")

# Calculate the temperature with the highest fraction
temperatures = np.linspace(3000, 9000, 700)
best_fraction = 0
best_temp = 0
for temp in temperatures:
    frac = getVisibleEnergyFraction(temp, spectrum_prep, T, ep)
    if best_fraction < frac:
        best_fraction = frac
        best_temp = temp

print(f"Best found temp T={best_temp:.4f} with a fraction of {best_fraction:.4f}")
