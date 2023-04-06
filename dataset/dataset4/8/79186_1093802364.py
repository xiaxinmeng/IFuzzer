def readdata(astr):
    if astr.startswith('@'):
        with open(astr[1:], 'r') as f:
            d = json.load(f)
            return d
    else:
        return astr