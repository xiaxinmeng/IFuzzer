# t.py
import pathlib
import sys

sys.path.append(pathlib.Path('foo'))

import s

# foo/s.py
print(123)