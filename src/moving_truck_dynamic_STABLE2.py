from openseespy.opensees import *
import numpy as np
import sys

speed = float(sys.argv[1])

dt = 0.001
L = 21.0
nEle = 60
dx = L / nEle

EI = 4.5645e9
E = 2.1e11
I = EI / E
A = 1.0

m_per_length = 1698.605
mnode = m_per_length * dx

F1 = -30e3
F2 = -80e3
Sp = 4.0

wipe()
model("basic", "-ndm", 2, "-ndf", 3)

# Nodes
for i in range(nEle + 1):
    node(i + 1, i * dx, 0.0)

# Supports
fix(1, 1, 1, 0)
fix(nEle + 1, 0, 1, 0)

geomTransf("Linear", 1)

# Elements
for i in range(1, nEle + 1):
    element("elasticBeamColumn", i, i, i + 1, A, E, I, 1)

# Mass: put mass in vertical DOF (DOF 2)
for i in range(1, nEle + 2):
    mass(i, 0.0, mnode, 0.0)

# Damping
rayleigh(1.1295, 0.0, 0.000251, 0.0)

# Analysis
system("BandGeneral")
constraints("Plain")
numberer("RCM")
test("NormDispIncr", 1e-6, 50)
algorithm("Linear")
integrator("Newmark", 0.6, 0.3025)
analysis("Transient")

t = 0.0
t_end = (L + Sp) / speed

midNode = int(nEle / 2) + 1
u_mid = []

step = 0
while t <= t_end:

    ts_tag = 100000 + step
    pat_tag = 200000 + step

    timeSeries("Linear", ts_tag)
    pattern("Plain", pat_tag, ts_tag)

    x1 = speed * t
    x2 = x1 - Sp

    for x, F in [(x1, F2), (x2, F1)]:
        if 0.0 <= x <= L:
            i = int(x / dx) + 1
            xi = (x - (i - 1) * dx) / dx
            if i < nEle:
                load(i, 0.0, F * (1 - xi), 0.0)
                load(i + 1, 0.0, F * xi, 0.0)

    ok = analyze(1, dt)

    remove("loadPattern", pat_tag)
    remove("timeSeries", ts_tag)

    if ok != 0:
        print("Analysis failed at t =", t)
        break

    u_mid.append(nodeDisp(midNode, 2))
    t += dt
    step += 1

peak = float(np.min(u_mid)) if len(u_mid) else 0.0

print("Simulation finished")
print("Speed =", speed, "m/s")
print("dt =", dt, "s")
print("Peak deflection =", peak, "m")