import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("midspan_response.txt")

time = data[:, 0]
disp = data[:, 1]

max_disp = np.min(disp)

print("Maximum midspan deflection =", max_disp, "m")

plt.figure(figsize=(8, 4))
plt.plot(time, disp, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Midspan deflection (m)")
plt.title("Midspan deflection under moving truck (20 m/s)")
plt.grid(True)
plt.tight_layout()
plt.savefig("midspan_deflection.png", dpi=300)
plt.show()
