from scipy.integrate import quad
from sympy import symbols, exp, lambdify

if __name__ == "__main__":
    a = symbols("a", positive=True)
    v = symbols("v")
    integrand = (3.0002 * (10 ** -8)) * (v ** 2) * exp(-1*a*(v**2))
    integrand_with_a = integrand.subs(a, 5.61428 * (10 ** -6))

    func_integrand = lambdify(v, integrand_with_a, "numpy")
    result, error = quad(func_integrand, 0, 300)
    print(f"Probability: {result}\nError: {error}")
