import numpy as np
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve

"""
This program calculates the wavelength that has the greatest energy in the Planck
Spectrum at T=300 K. It also plots the distribution at this temperature.
"""

# Constants
k_J = 1.381 * pow(10,-23)      # J / K
k_ev = 8.617 * pow(10,-5)      # eV / K
h = 6.626 * pow(10, -34)       # J s
G = 6.674 * pow(10, -11)       # N m^2 / kg^2
m_e = 9.109 * pow(10, -31)     # kg              mass of electron
m_p = 1.673 * pow(10, -27)     # kg              mass of proton
avogadro = 6.022 * pow(10, 23) # unitless


temp = 300 # K

h, c, lam, k, T, x = symbols("h c lamda, k, T x", positive=True)

spectrum = 8 * pi * h * c / lam ** 5
spectrum *= 1 / (exp(h * c / (lam * k * T)) - 1)
print(f"Wavelength Spectrum: {spectrum}")

spectrum = spectrum.subs(lam, x * h * c / (k * T)) # Make dimensionless substitution
print(f"Substituted Wavelength Spectrum: {spectrum}")

spectrum_deriv = diff(spectrum, x)
print(f"Wavelength Spectrum Derivative: {spectrum_deriv}")

# TODO: Getting not implemented error. Try defining x such that we get e^x instead
# of e^1/x, and then invert the solution instead or something like that.
soln = solve(spectrum_deriv, x)
print(f"Critical Points: {soln}")
