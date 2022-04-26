from math import log, exp

def acceptance_ratio(V1, V2, vol1, vol2, N, P, beta):
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
