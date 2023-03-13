import numpy as np

def minimum_image(r, L):
    # possibly required for spring
    # but also possibly can be neglected (i hope...)
    return r - L * np.round(r / L)

def spring_potential(r, beta, tp):
    val = r - np.roll(r, 1, axis=0)
#    val = minimum_image(val, L)
    return 0.5 * np.sum(val**2) / beta / tp

def get_rc(path):
    # path has shape (M, N, 3)
    return 0.5 * (np.roll(path, 1, axis=0) + np.roll(path, -1, axis=0))

def spring_force(r, rc, beta, tp):
    # force from spring_potential()
#    return 2 * minimum_image(rc - r, L) / beta / tp
    return 2 * (rc - r) / beta / tp

def rescale_path(r, old_L, new_L):
    # for NPT
    # should mimic behavior of scale_atoms=True in ASE
    # r has shape (M, N, 3)
    # old_L and new_L are either floats (for cubic)
    # or both have shape (3,) (for orthorhombic)
    # both work because of numpy's broadcasting along last axis (?)
    return r * new_L / old_L
