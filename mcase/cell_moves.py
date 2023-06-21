import numpy as np
from math import log, exp

def log_T(L1, L2, P, N, s, beta, tau):
    """
    probability of going from L1 to L2
    where s is the stress calculated at L1

    args:
        L1 (array): initial lengths, shape (3,)
        L2 (array): final lengths, shape (3,)
        P (float): pressure
        N (int): number of particles
        s (array): diagonal stresses, shape (3,)
        beta (float): inverse temperature
        tau (float): time step
    returns:
        float: log of transition probability,
            without the irrelevant normalization
    """
    volume = np.prod(L1)
    val = N - beta*volume*(P + s)
    val *= (tau / L1)
    val = L2 - L1 - val
    val = np.sum(val**2)
    val /= -4*tau
    return val

def acceptance_ratio(L1, L2, V1, V2, s1, s2, N, P, beta, tau):
    """
    acceptance ratio for cell move

    args:
        L1 (array): initial lengths, shape (3,)
        L2 (array): final lengths, shape (3,)
        V1 (float): initial energy
        V2 (float): final energy
        s1 (array): stresses at L1, shape (3,)
        s2 (array): stresses at L2, shape (3,)
        N (int): number of particles
        P (float): pressure (units should be consistent with V and vol)
        beta (float): inverse temperature
        tau (float): time step
    returns:
        float: acceptance ratio
    """
    vol1 = np.prod(L1)
    vol2 = np.prod(L2)
    T1 = log_T(L1, L2, P, N, s1, beta, tau)
    T2 = log_T(L2, L1, P, N, s2, beta, tau)
    val = P*(vol2 - vol1) + V2 - V1
    val *= -beta
    val += N*log(vol2/vol1)
    return exp(T2 - T1 + val)

def old_acceptance_ratio(V1, V2, vol1, vol2, N, P, beta):
    """
    acceptance ratio for cell move

    args:
        V1 (float): initial energy
        V2 (float): final energy
        vol1 (float): initial volume
        vol2 (float): final volume
        N (int): number of particles
        P (float): pressure (units should be consistent with V and vol)
        beta (float): inverse temperature
    returns:
        float: acceptance ratio
    """
    val = P*(vol2 - vol1) + V2 - V1
    val *= -beta
    val += N*log(vol2/vol1)
    return exp(val)
