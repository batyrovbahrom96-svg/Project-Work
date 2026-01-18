from bridge_dynamic_base import build_bridge_model, add_lumped_mass, set_rayleigh_damping
import math

L = 21.0
nEle = 40
EI = 4564504658.681315

build_bridge_model(L=L, nEle=nEle, EI=EI)
m_per_len = add_lumped_mass(L=L, nEle=nEle)

f1, f2, alphaM, betaK = set_rayleigh_damping(zeta=0.02, num_modes=2)

Sp = 4.0
v_res_1 = f1 * Sp
v_res_2 = f2 * Sp

print("Mass per length =", m_per_len, "kg/m")
print("Mode 1 frequency f1 =", f1, "Hz")
print("Mode 2 frequency f2 =", f2, "Hz")
print("Rayleigh alphaM =", alphaM)
print("Rayleigh betaK  =", betaK)
print("Resonance estimate using spacing Sp=4 m:")
print("v ~ f1*Sp =", v_res_1, "m/s")
print("v ~ f2*Sp =", v_res_2, "m/s")