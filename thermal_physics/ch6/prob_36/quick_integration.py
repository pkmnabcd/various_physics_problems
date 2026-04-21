from sympy import symbols, exp, oo, integrate

if __name__ == "__main__":
    a = symbols("a", positive=True)
    v = symbols("v")
    integrand = (v ** 3) * exp(-1*a*(v**2))
    result = integrate(integrand, (v, 0, oo))
    print(result)
