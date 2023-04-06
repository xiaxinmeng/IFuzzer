
from unittest import mock
import multiprocessing


def identity(x):
    return x

with multiprocessing.Pool() as pool:
    multiprocessed = list(pool.map(identity, [mock.sentinel.foo]))

assert identity(mock.sentinel.foo) == mock.sentinel.foo  # Passes
assert multiprocessed[0] == mock.sentinel.foo  # Fails
