from sympy import symbols, exp, oo, integrate, simplify

if __name__ == "__main__":
    ep = symbols("ep")
    mu = symbols("mu", real=True)
    k = symbols("k", positive=True)
    T = symbols("T", positive=True)
    g = symbols("g", positive=True)

    integrand = g / ( exp((ep - mu) / (k * T)) + 1 )
    print(f"Integrand: {integrand}")
    result = integrate(integrand, (ep, 0, oo))
    print(f"Result: {result}")
    simplified = simplify(result)
    print(f"Simplified Result: {simplified}")
