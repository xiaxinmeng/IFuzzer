from functools import partial

with open('...', 'rb') as f:
    for block in iter(partial(f.read, 4096), b''):
        ...