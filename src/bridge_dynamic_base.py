from openseespy.opensees import *
import math

def build_bridge_model(L=21.0, nEle=40, EI=4564504658.681315):
    wipe()
    model("basic", "-ndm", 2, "-ndf", 3)

    Le = L / nEle

    A = 1.0
    E = EI
    I = 1.0

    for i in range(nEle + 1):
        x = Le * i
        node(i + 1, x, 0.0)

    fix(1, 1, 1, 0)
    fix(nEle + 1, 0, 1, 0)

    geomTransf("Linear", 1)

    for i in range(1, nEle + 1):
        element("elasticBeamColumn", i, i, i + 1, A, E, I, 1)

    return Le

def add_lumped_mass(L=21.0, nEle=40):
    Le = L / nEle

    rho_c = 2500.0
    rho_s = 7850.0

    A_conc = 2.0 * 0.3
    A_steel = (1.37 * 0.01) + 2.0 * (0.29 * 0.02)

    m_per_len = rho_c * A_conc + rho_s * A_steel

    for i in range(nEle + 1):
        tag = i + 1
        m = m_per_len * Le
        if i == 0 or i == nEle:
            m = 0.5 * m
        mass(tag, m, m, 0.0)

    return m_per_len

def set_rayleigh_damping(zeta=0.02, num_modes=2):
    lambdas = eigen(num_modes)
    w = [math.sqrt(lmbd) for lmbd in lambdas]

    w1 = w[0]
    w2 = w[1] if len(w) > 1 else w[0] * 3.0

    a11 = 1.0 / (2.0 * w1)
    a12 = w1 / 2.0
    a21 = 1.0 / (2.0 * w2)
    a22 = w2 / 2.0

    det = a11 * a22 - a12 * a21
    alphaM = (zeta * a22 - zeta * a12) / det
    betaK  = (zeta * a11 - zeta * a21) / det

    rayleigh(alphaM, 0.0, 0.0, betaK)

    f1 = w1 / (2.0 * math.pi)
    f2 = w2 / (2.0 * math.pi)

    return f1, f2, alphaM, betaK
