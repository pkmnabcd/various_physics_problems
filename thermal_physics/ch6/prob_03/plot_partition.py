import numpy as np
import matplotlib.pyplot as plt
from math import pow

# Boltzman's const in eV / K
k = (1.3806 * pow(10,-23)) * (6.242 * pow(10,18))

temp = np.linspace(1, 300_000, 1000)
z = 1 + np.exp(-1*2 / (k * temp))

plt.plot(temp, z)
plt.title("Temp vs Partition Function for 2-state system", wrap=True)
plt.xlabel("Temp (K)")
plt.ylabel("Partition Function Z")
plt.savefig("temp_vs_partition.png")


temp = np.array([300., 3000., 30_000., 300_000.])
z = 1 + np.exp(-1*2 / (k * temp))

for i in range(len(temp)):
    print(f"Temp: {temp[i]}\nPartition Function: {z[i]}\n")
