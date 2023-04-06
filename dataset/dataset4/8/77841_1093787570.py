import os
import pathlib

# Change to the Root directory
os.chdir('/')

# Create a relative path object.
p = pathlib.Path('spam')
print(p.resolve())