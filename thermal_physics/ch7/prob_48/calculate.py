import numpy as np
import math
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve, lambdify
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
This program does the numerical integration for a part
of the equation of U/V for a neutrino gas. It also does
a similar integral for N/V. I also compute N/V for a
specific temperature.
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


# Evaluate the integral for the energy density
x = symbols("x", positive=True)
integrand = x ** 3 / ( exp(x) + 1 )
integrand_lambda = lambdify(x, integrand, "numpy")
result, error = quad(integrand_lambda, 0, np.inf)
print(f"Integration result: {result:e}\n\t with error {error:e}.")

# Evaluate the integral for the energy density
integrand = x ** 2 / ( exp(x) + 1 )
integrand_lambda = lambdify(x, integrand, "numpy")
result, error = quad(integrand_lambda, 0, np.inf)
print(f"Integration result: {result:e}\n\t with error {error:e}.")

# Calculate N/V for T=1.95 K
temp = 1.95
neutrino_num_density = 24 * Const.pi * (Const.k_J * temp / Const.h / Const.c) ** 3 * result
print(f"Neutrino number density: {neutrino_num_density:e} particles/m^3")
