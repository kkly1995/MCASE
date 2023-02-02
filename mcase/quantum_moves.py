import numpy as np

def minimum_image(r, L):
    # possibly required for spring
    # but also possibly can be neglected (i hope...)
    return r - L * np.round(r / L)

def spring_potential(r, beta, tp):
    val = r - np.roll(r, 1, axis=0)
#    val = minimum_image(val, L)
    return 0.5 * np.sum(val**2) / beta / tp

def spring_force(r, rc, beta, tp):
    # force from spring_potential()
#    return 2 * minimum_image(rc - r, L) / beta / tp
    return 2 * (rc - r) / beta / tp
