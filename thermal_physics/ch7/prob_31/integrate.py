from sympy import symbols, exp, oo, integrate, simplify, latex, Rational

if __name__ == "__main__":
    ep = symbols("epsilon", positive=True)
    mu = symbols("mu", negative=True)
    k, T = symbols("k T", positive=True)

    integrand = ep * exp(-1*(ep-mu)/(k*T))
    result = integrate(integrand, (ep, 0, oo))
    print(f"Integrand: {integrand}")
    print(f"Result: {result}")
    print(f"Result Latex: {latex(result)}")
