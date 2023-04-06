
import subprocess

cwd = 'x' * 10**6
for __ in range(100):
    try:
        subprocess.call(['/xxx'], cwd=cwd, user=2**64)
    except OverflowError:
        pass

from resource import *
print(getrusage(RUSAGE_SELF).ru_maxrss)
