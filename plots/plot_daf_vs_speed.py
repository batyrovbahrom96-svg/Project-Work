import numpy as np
import matplotlib.pyplot as plt

# Load CSV from daf_from_modal.py
data = np.loadtxt("daf_vs_speed_v2.csv", delimiter=",", skiprows=1)
speeds = data[:, 0]
daf = data[:, 2]

# From your Day 6 modal check
v_res_1 = 23.355646624065937  # m/s (f1 * Sp)

plt.figure()
plt.plot(speeds, daf, marker="o")
plt.axvline(v_res_1, linestyle="--")
plt.title("DAF vs Speed (Rayleigh damping, moving truck)")
plt.xlabel("Speed (m/s)")
plt.ylabel("DAF")
plt.grid(True)
plt.show()