import os
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dir:
    os.chdir(dir)