from openseespy.opensees import *

wipe()
model("basic", "-ndm", 2, "-ndf", 3)

L = 21.0
nEle = 60
Le = L / nEle

# Use real E and I
EI = 4.564504658681315e9
E = 2.0e11
I = EI / E
A = 0.11447623001674831

# Nodes
for i in range(nEle + 1):
    node(i + 1, i * Le, 0.0)

# Supports
fix(1, 1, 1, 0)
fix(nEle + 1, 0, 1, 0)

geomTransf("Linear", 1)

# Elements
for i in range(1, nEle + 1):
    element("elasticBeamColumn", i, i, i + 1, A, E, I, 1)

timeSeries("Linear", 1)
pattern("Plain", 1, 1)

# Truck loads
F1 = -30e3
F2 = -80e3
Sp = 4.0

mid = int((nEle + 1) / 2)
dN = int(round(Sp / Le))

load(mid, 0.0, F2, 0.0)
load(mid - dN, 0.0, F2, 0.0)
load(mid + dN, 0.0, F1, 0.0)

# Analysis settings for a linear problem
system("BandGeneral")
constraints("Plain")
numberer("RCM")
test("NormUnbalance", 1e-12, 50)
algorithm("Linear")
integrator("LoadControl", 1.0)
analysis("Static")

ok = analyze(1)

if ok != 0:
    print("Static analysis failed, code =", ok)
else:
    u_static = nodeDisp(mid, 2)
    print("Static deflection =", u_static, "m")
