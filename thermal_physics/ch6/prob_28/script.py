from sympy import symbols, summation, exp, diff, log

upper_j = 6


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

    # TODO: get unitless variable, subs it, get lambda, plot
