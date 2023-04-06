import importlib.metadata
import sys
import time


# moved outside of the loop, already showed this component is slower
eps = importlib.metadata.entry_points()
def f():
    # common for plugin systems to look up multiple entry points
    for ep in ('console_scripts', 'flake8.extension', 'pytest11'):
        if sys.version_info >= (3, 10):
            eps.select(name=ep)
        else:
            eps[ep]


t0 = time.time()
for _ in range(10000):
    f()
t1 = time.time()
print(f'{t1-t0}')