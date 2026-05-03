from sympy import symbols, exp, oo, integrate

if __name__ == "__main__":
    x = symbols("x")
    integrand = x * exp(-1*(x**2))
    result = integrate(integrand, (x, 0, oo))
    print(result)
