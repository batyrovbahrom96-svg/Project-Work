import subprocess
import re
import numpy as np

# Static reference deflection
u_static = 0.0071413997859050525  # your validated static result

speeds = list(range(2, 42, 2))  # 2,4,...,40
peaks = []
dafs = []

for v in speeds:
    print(f"Running speed = {v} m/s")

    cmd = ["arch", "-x86_64", "python3", "moving_truck_dynamic_STABLE2.py", str(v)]
    out = subprocess.check_output(cmd, universal_newlines=True)

    m = re.search(r"Peak deflection = ([\-0-9\.eE]+)", out)
    if not m:
        print("Could not parse output")
        continue

    peak = abs(float(m.group(1)))
    daf = peak / abs(u_static)

    peaks.append(peak)
    dafs.append(daf)

    print(f"  Peak = {peak:.6f} m, DAF = {daf:.3f}")

# Save CSV
data = np.column_stack((speeds, peaks, dafs))
np.savetxt("daf_results.csv", data, delimiter=",", header="Speed,PeakDeflection,DAF", comments="")

print("\nFINAL RESULTS")
print("Speeds:", speeds)
print("Peaks:", peaks)
print("DAFs:", dafs)
print("\nSaved to daf_results.csv")
