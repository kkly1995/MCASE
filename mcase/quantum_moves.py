import numpy as np

def minimum_image(r, L):
    # possibly required for spring
    # but also possibly can be neglected (i hope...)
    return r - L * np.round(r / L)

def spring_potential(r, rc, beta, tp):
    # contribution to quantum spring potential from a SINGLE slice
    val = np.sum(r**2 - 2 * r * rc)
    return val / beta / tp

def spring_force(r, rc, beta, tp):
    # force from spring_potential(), on single slice
    return 2 * (rc - r) / beta / tp
