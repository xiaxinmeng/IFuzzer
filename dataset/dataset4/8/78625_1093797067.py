
import os
import sys

sys.path.insert(0, '.')

# Importing it before chdir already causes failure.
import imported

os.chdir('/')
print(imported.__file__)  # ./imported.py
assert imported.__file__ == os.path.abspath(imported.__file__)
