from sympy import symbols, exp, oo, integrate, simplify, latex

if __name__ == "__main__":
    ep = symbols("epsilon", real=True)
    mu = symbols("mu", real=True)


    # First, get taylor expansion of epsilon centered on mu
    ep_to_power = ep ** (5/2)
    print(f"Expression: {ep_to_power}")
    series_expansion = ep_to_power.series(ep, mu, 3)
    print(f"Expansion: {series_expansion}")
    print(f"Expansion Latex: {latex(series_expansion)}")






    #mu = symbols("mu", real=True)
    #k = symbols("k", positive=True)
    #T = symbols("T", positive=True)
    #g = symbols("g", positive=True)

    #integrand = g / ( exp((ep - mu) / (k * T)) + 1 )
    #print(f"Integrand: {integrand}")
    #result = integrate(integrand, (ep, 0, oo))
    #print(f"Result: {result}")
    #simplified = simplify(result)
    #print(f"Simplified Result: {simplified}")
