import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("daf_results.csv", delimiter=",", skiprows=1)

speeds = data[:, 0]
peaks = data[:, 1]
dafs = data[:, 2]

plt.figure()
plt.plot(speeds, dafs, marker="o")
plt.xlabel("Speed (m/s)")
plt.ylabel("Dynamic Amplification Factor (DAF)")
plt.title("DAF vs Vehicle Speed")
plt.grid(True)
plt.show()
