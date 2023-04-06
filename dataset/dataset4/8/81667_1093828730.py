
from pathlib import Path

p = Path('.')

assert p == p.parent # should fail but it does not
