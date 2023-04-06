import os
orig_spawnve = os.spawnve

def log_spawnve(*args):
    print("spawnve: %r" % (args,))
    return orig_spawnve(*args)

os.spawnve = log_spawnve