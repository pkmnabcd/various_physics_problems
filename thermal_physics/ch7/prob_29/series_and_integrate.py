from sympy import symbols, exp, oo, integrate, simplify, latex, Rational

if __name__ == "__main__":
    ep = symbols("epsilon", real=True)
    #mu = symbols("mu", real=True)
    mu = symbols("mu", positive=True)


    # First, get taylor expansion of epsilon centered on mu
    ep_to_power = ep ** Rational(5,2)
    print(f"Expression: {ep_to_power}")
    series_expansion = ep_to_power.series(ep, mu, 3)
    print(f"Expansion: {series_expansion}")
    print(f"Expansion Latex: {latex(series_expansion)}")
