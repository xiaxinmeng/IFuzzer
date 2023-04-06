def unique_cols(filename):
    cols = next(csv.reader(open(filename,'r')))
    return len(cols) == len(set(cols))