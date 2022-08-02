# load table for pair potential
import numpy as np
from scipy.interpolate import interp1d

def read_table(fname):
    # look for the line starting with N
    # then the rest of the file should be the table
    # returns two interpolation objects,
    # the pair energy as a function of distance
    # and the corresponding force as a function of distance
    # for distances not covered by the table, the interpolations
    # will return 0 (enforced by fill_value=0?)
    with open(fname, 'r') as f:
        while f.readline()[0] != 'N': # N is assumed to be first char
            pass
        data = np.loadtxt(f)
    energy = interp1d(data[:,1], data[:,2],\
            bounds_error=False, fill_value=0)
    force = interp1d(data[:,1], data[:,3],\
            bounds_error=False, fill_value=0)
    return energy, force

def evaluate(pairs, energy, force):
    # pairs is the pair table
    # ideally taken from get_all_distances(mic=True, vector=True)
    # np.linalg.norm is assumed to be faster than calling it again
    norm = np.linalg.norm(pairs, axis=-1)
    energy_table = energy(norm)
    force_table = force(norm)
    total_energy = 0.5*np.sum(energy_table)
    # forces are a little trickier
    norm[np.diag_indices_from(norm)] = 1 # avoid division by zero
    force_table /= norm
    force_table = force_table[:,:,np.newaxis]*pairs
    total_forces = np.sum(force_table, axis=0)
    return total_energy, total_forces

def subtract(samples, energy, force):
    # for prepping data
    # returns the samples with pair potential subtracted off
    # no stresses / virials
    from ase.calculators.singlepoint import SinglePointCalculator
    new_samples = []
    for i in range(len(samples)):
        pairs = samples[i].get_all_distances(mic=True, vector=True)
        e, f = evaluate(pairs, energy, force)
        # replace
        new_sample = samples[i].copy()
        new_calc = SinglePointCalculator(new_sample,
                energy = samples[i].get_potential_energy() - e,
                forces = samples[i].get_forces() - f,
                stress = None
                )
        new_sample.calc = new_calc
        new_samples.append(new_sample)
    return new_samples
