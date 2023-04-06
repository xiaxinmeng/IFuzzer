import importlib.metadata
import sys
import time


def f():
    eps = importlib.metadata.entry_points()
    if sys.version_info >= (3, 10):
        eps.select(name='console_scripts')
    else:
        eps['console_scripts']


t0 = time.time()
for _ in range(100):
    f()
t1 = time.time()
print(f'{t1-t0}')