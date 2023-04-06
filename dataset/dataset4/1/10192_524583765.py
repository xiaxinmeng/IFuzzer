
from unittest.mock import Mock
from random import Random
import sys

prng = Random()
prng._randbelow = Mock(wraps=prng._randbelow)

n, k = map(int, sys.argv[1:3])
prng.sample(range(n), k)
rbc = prng._randbelow.call_count
print(f'randbelow_calls={rbc} <-- n={n} k={k}')
