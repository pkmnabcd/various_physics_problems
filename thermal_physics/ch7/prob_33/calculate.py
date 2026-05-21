import numpy as np
from math import pow, pi, log, exp

# Constants
k_J = 1.381 * pow(10,-23)      # J / K
k_ev = 8.617 * pow(10,-5)      # eV / K
h = 6.626 * pow(10, -34)       # J s
G = 6.674 * pow(10, -11)       # N m^2 / kg^2
m_e = 9.109 * pow(10, -31)     # kg              mass of electron
m_p = 1.673 * pow(10, -27)     # kg              mass of proton
avogadro = 6.022 * pow(10, 23) # unitless


T = 300 # K

exp_term = exp(-1.11 / (2 * k_ev * T))
V = 1 * pow(10, -6) # m^3
mid_term = pow(8 * pi * m_e * k_J * T, 3/2) / (4 * pow(h, 3))

N_c = V * mid_term * exp_term
print(f"N_c = {N_c:e}")
print(f"Mid Term: {mid_term:e}")
