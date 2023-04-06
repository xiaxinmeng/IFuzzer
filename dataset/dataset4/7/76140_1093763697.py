
import os
from tempfile import TemporaryDirectory

name = TemporaryDirectory().name
print(os.path.exists(name))  # prints False

td = TemporaryDirectory()
name_2 = td.name
print(os.path.exists(name_2))  # prints True
