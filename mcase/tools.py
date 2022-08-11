import numpy as np

def read_thermo(fname):
    """
    read numeric data from output

    args:
        fname (str): name of output file
    returns:
        array: can have different shapes depending on the calculation
    """
    with open(fname, 'r') as f:
        # its easier to just read the whole thing first
        lines = f.readlines()
    # find number of samples
    for line in lines:
        words = line.split()
        if words[0] == 'number':
            N = int(words[-1])
            break
    # find where the data begins
    linenum = -1
    i = 0
    while linenum < 0:
        try:
            words = lines[i].split()
            x = float(words[0])
            # if this succeeds then this should be the data
            linenum = i
        except:
            i += 1
    # can now get data
    return np.loadtxt(fname, skiprows=i, max_rows=N)

def get_meta(fname):
    # placeholder, plan to implement
    pass

def make_input(fname, meta):
    # placeholder, plan to implement
    pass
