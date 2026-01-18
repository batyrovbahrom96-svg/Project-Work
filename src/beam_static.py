from openseespy.opensees import *
import numpy as np

wipe()
model("basic", "-ndm", 2, "-ndf", 3)

L = 20.0
nEle = 40
E = 2.1e11
A = 0.02
I = 8e-4

node(1, 0.0, 0.0)
node(nEle + 1, L, 0.0)

for i in range(2, nEle + 1):
    x = L * (i - 1) / nEle
    node(i, x, 0.0)

fix(1, 1, 1, 0)
fix(nEle + 1, 0, 1, 0)

geomTransf("Linear", 1)

for i in range(1, nEle + 1):
    element("elasticBeamColumn", i, i, i + 1, A, E, I, 1)

timeSeries("Linear", 1)
pattern("Plain", 1, 1)

midNode = int((nEle + 2) / 2)
load(midNode, 0.0, -10000.0, 0.0)

system("BandGeneral")
constraints("Plain")
numberer("RCM")
integrator("LoadControl", 1.0)
algorithm("Newton")
analysis("Static")
analyze(1)

dispMid = nodeDisp(midNode, 2)
print("Midspan deflection =", dispMid, "m")