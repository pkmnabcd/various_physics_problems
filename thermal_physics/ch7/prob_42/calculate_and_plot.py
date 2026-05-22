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
    k_ev = 8.617 * pow(10,-5)      # eV / K
    h = 6.626 * pow(10, -34)       # J s
    G = 6.674 * pow(10, -11)       # N m^2 / kg^2
    c = 2.998 * pow(10, 8)         # m / s

    # Other Constants
    m_e = 9.109 * pow(10, -31)     # kg              mass of electron
    m_p = 1.673 * pow(10, -27)     # kg              mass of proton
    avogadro = 6.022 * pow(10, 23) # unitless

    # Math Constants
    pi = math.pi


# TODO: Make the program. The following was copied from 7.42 and is for reference

# Find the peak wavelength for T=300 K
temp = 300 # K
h, c, lam, k, T, x = symbols("h c lamda, k, T x", positive=True)

spectrum = 8 * pi * h * c / lam ** 5
spectrum *= 1 / (exp(h * c / (lam * k * T)) - 1)
print(f"Wavelength Spectrum: {spectrum}")

spectrum_x = spectrum.subs(lam, h * c / (x * k * T)) # Make dimensionless substitution
print(f"Substituted Wavelength Spectrum: {spectrum_x}")

spectrum_deriv = diff(spectrum_x, x)
print(f"Wavelength Spectrum Derivative: {spectrum_deriv}")

solutions = solve(spectrum_deriv, x)
soln = solutions[0].evalf()
lambda_peak = Const.h * Const.c / (soln * Const.k_J * temp)
print(f"Peak Wavelength: {lambda_peak:e} m")



# Plot the spectrum
spectrum_prep = spectrum.subs(h, Const.h).subs(c, Const.c).subs(k, Const.k_J).subs(T, temp)
spectrum_lambda = lambdify(lam, spectrum_prep, "numpy")
lambda_array = np.linspace(pow(10, -12), 5*pow(10, -5), 10_000)
spectrum_array = spectrum_lambda(lambda_array)
plt.plot(lambda_array, spectrum_array)
plt.title(f"Planck Spectrum for T={temp} K")
plt.xlabel("Wavelength (m)")
plt.ylabel("Energy Density Per Photon Wavelength (J/m^4)")
plt.savefig("lambda_vs_spectrum.png")
