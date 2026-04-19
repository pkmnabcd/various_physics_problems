import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, summation, exp, diff, log, simplify, lambdify

upper_j = 6
t_start = 0
t_end = 3


if __name__ == "__main__":
    # Getting Z
    k, T, j, ep = symbols("k T j ep") # ep is epsilon
    expr = ((2*j) + 1) * exp(-1*j*(j+1) * ep / (k*T))
    Z = summation(expr, (j, 0, upper_j))
    print(f"Z approximated with j in [0,{upper_j}]")
    print(Z)
    print()

    # Getting average E
    beta = symbols("beta")
    z_with_beta = Z.subs(1/(k*T), beta)
    avg_E = -1 * diff(log(z_with_beta), beta)
    print("Average Energy:")
    print(avg_E)
    print()

    # Getting Heat Capacity
    avg_E_with_kT = avg_E.subs(beta, 1/(k*T))
    C = diff(avg_E_with_kT, T)
    print("Heat Capacity:")
    print(C)
    print()

    # Put in unitless variable
    t = symbols("t")
    c_in_t = C.subs(T, t*ep/k)
    c_unitless = simplify(c_in_t / k)

    # Get numpy function
    t_vals = np.linspace(t_start, t_end, num=200)
    c_over_k_lambda = lambdify(t, c_unitless, "numpy")
    # NOTE: small t will cause /0 and overflow errors, but it's fine :)
    c_over_k_vals = c_over_k_lambda(t_vals)

    # Plot the results
    plt.plot(t_vals, c_over_k_vals)
    plt.title(f"Rotational Heat Capacity when j in [0,{upper_j}]")
    plt.xlabel("Reduced Temperature (kT/epsilon)")
    plt.ylabel("Heat Capacity (C/k)")
    plt.savefig("reduced_temp-heat_capacity_curve.png")

    plt.close()
