import numpy as np
import math
from math import pow, log
from sympy import symbols, exp, oo, integrate, simplify, latex, Rational, pi, diff, solve, lambdify
import matplotlib.pyplot as plt
from scipy.integrate import quad

"""
This program does the numerical integration for a part
of the equation of N for a photon gas. It also does a
small calculation and calculates the number of photons
at several temperatures.
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


# Evaluate the integral of the number of photons
x = symbols("x", positive=True)
integrand = x ** 2 / ( exp(x) - 1 )
integrand_lambda = lambdify(x, integrand, "numpy")
result, error = quad(integrand_lambda, 0, np.inf)
print(f"Integration result: {result:e}\n\t with error {error:e}.")

# Calculate entropy per photon times k
res = 4 * Const.pi ** 4 / 45 / result
print(f"Entropy per photon is {res:e} * k")

# Calculate N for different temps
temps = np.array([2.73, 300, 1500])
N = 8 * Const.pi * (Const.k_J * temps / Const.h / Const.c) ** 3 * result
for i in range(len(temps)):
    print(f"Temp: {temps[i]} K with N: {N[i]:e}")
