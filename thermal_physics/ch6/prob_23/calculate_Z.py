from math import pow, e

K = 8.617 * pow(10, -5) # Boltzmann's constantt in eV / K

if __name__ == "__main__":
    epsilon = 0.00024 # eV
    T = 300           # K
    final_j = 40

    result = 0
    for j in range(final_j+1): # j has range [0,final_j]
        result += (2*j + 1) * pow(e, -1 * j * (j+1) * epsilon / (K * T))

    print(f"For j in [0,{final_j}], Z = {result:.3f}")
