
def _to_number(x):
    if isinstance(x, str):
        if '.' in x:
            x = float(x)
        else:
            x = int(x)
    return x
