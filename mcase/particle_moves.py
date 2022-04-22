import numpy as np

def log_T(r1, r2, f, beta, tau):
    """
    probability of going from r1 to r2
    where f is the force calculated at r1

    args:
        r1 (array): initial coordinates, any shape
        r2 (array): final coordinates, same shape as r1
        f (array): forces at r1, same shape as r1
        beta (float): inverse temperature
        tau (float): time step
    returns:
        float: log of transition probability,
            without the irrelevant normalization
    """
    val = r2 - r1 - tau*beta*f
    val = np.sum(val**2)
    val /= -4*tau
    return val

def acceptance_ratio(r1, r2, V1, V2, f1, f2, beta, tau):
    """
    acceptance ratio for particle move

    args:
        r1 (array): initial coordinates, any shape
        r2 (array): final coordinates, same shape as r1
        V1 (float): initial energy at r1
        V2 (float): final energy at r2
        f1 (array): forces at r1, same shape as r1
        f2 (array): forces at r2, same shape as r1
        beta (float): inverse temperature
        tau (float): time step
    returns:
        float: acceptance ratio
    """
    T1 = log_T(r1, r2, f1, beta, tau)
    T2 = log_T(r2, r1, f2, beta, tau)
    return np.exp(T2 - T1 - beta*(V2 - V1))
