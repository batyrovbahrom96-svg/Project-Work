import numpy as np

# Given geometry
b_deck = 2.0      # m
t_deck = 0.30     # m

b_flange = 0.29   # m
t_flange = 0.02   # m

h_web = 1.37      # m
t_web = 0.01      # m

# Material
fc = 40e6
Es = 200e9

# Concrete modulus (ACI)
Ec = 4700 * np.sqrt(fc / 1e6) * 1e6

# Modular ratio
n = Es / Ec

# Areas
Ac = b_deck * t_deck
At = b_flange * t_flange
Ab = b_flange * t_flange
Aw = h_web * t_web

As = At + Ab + Aw
Aeq_c = Ac / n
Aeq_total = As + Aeq_c

# Centroids (from bottom)
yb = t_flange / 2
yw = t_flange + h_web / 2
yt = t_flange + h_web + t_flange / 2
yc = t_flange + h_web + t_flange + t_deck / 2

# Neutral axis
yNA = (Ab * yb + Aw * yw + At * yt + Aeq_c * yc) / Aeq_total

# Local inertias
Ib = (b_flange * t_flange**3) / 12
It = Ib
Iw = (t_web * h_web**3) / 12
Ic = (b_deck * t_deck**3) / (12 * n)

# Parallel axis
Ieq = (
    Ib + Ab * (yb - yNA)**2 +
    Iw + Aw * (yw - yNA)**2 +
    It + At * (yt - yNA)**2 +
    Ic + Aeq_c * (yc - yNA)**2
)

# Equivalent EI
EI = Es * Ieq

print("Ec =", Ec)
print("Modular ratio n =", n)
print("Neutral axis yNA =", yNA)
print("Equivalent area Aeq =", Aeq_total)
print("Equivalent I =", Ieq)
print("Equivalent EI =", EI)