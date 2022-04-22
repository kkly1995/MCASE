def read_input(fname):
    """
    parse input file
    currently: just collects every line into a dict
    no matter what the names are
    and the names will be filtered out later when setting up a run

    args:
        fname (str): name of file to read
    returns:
        dict
    """
    parameters = {}
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        words = line.split()
        try:
            parameters[words[0]] = words[1]
        except:
            print('failed to read the following line from input:')
            print(line)
    return parameters
