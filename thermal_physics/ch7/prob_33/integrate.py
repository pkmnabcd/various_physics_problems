from sympy import symbols, exp, oo, integrate, simplify, latex, Rational

if __name__ == "__main__":
    x = symbols("x", real=True)

    integrand = x ** Rational(1, 2) * exp(-x)
    result = integrate(integrand, (x, 0, oo))
    print(f"Integrand: {integrand}")
    print(f"Result: {result}")
    print(f"Result Latex: {latex(result)}")
