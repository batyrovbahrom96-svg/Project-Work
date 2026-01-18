from openseespy.opensees import *
import numpy as np

wipe()
model("basic", "-ndm", 2, "-ndf", 3)

# Geometry
L = 21.0
nEle = 80

# Section properties
E = 2.0e11
A = 0.11447623001674831
I = 0.022822523293406578

# Create nodes
for i in range(nEle + 1):
    x = L * i / nEle
    node(i + 1, x, 0.0)

# Supports
fix(1, 1, 1, 0)               # pin
fix(nEle + 1, 0, 1, 0)       # roller

# Transformation
geomTransf("Linear", 1)

# Elements
for i in range(1, nEle + 1):
    element("elasticBeamColumn", i, i, i + 1, A, E, I, 1)

# Load
timeSeries("Linear", 1)
pattern("Plain", 1, 1)

mid = int((nEle + 1) / 2)

P = -100e3   # 100 kN point load
load(mid, 0.0, P, 0.0)

# Analysis
system("BandGeneral")
constraints("Plain")
numberer("RCM")
test("NormDispIncr", 1e-12, 100)
algorithm("Newton")
integrator("LoadControl", 0.1)
analysis("Static")

ok = analyze(10)

if ok != 0:
    print("Analysis failed, trying ModifiedNewton")
    algorithm("ModifiedNewton")
    ok = analyze(10)

if ok != 0:
    print("Still failed, error code =", ok)

# Output
dispMid = nodeDisp(mid, 2)
print("Midspan deflection =", dispMid, "m")