import shutil
import os
import tempfile
from subprocess import call


def create_dirlink(existing, new_link):
    # This works if /D is used, but fails for junctions:
    call(['mklink', '/J', new_link, existing], shell=True)


root = tempfile.mkdtemp()

# Create two subdirs, a and b
os.mkdir(os.path.join(root, 'a'))
os.mkdir(os.path.join(root, 'b'))

# Create a directory link in 'X', pointing to 'Y'
# This works:
# create_dirlink(os.path.join(root, 'b'), os.path.join(root, 'a', 'link'))
# This doesn't:
create_dirlink(os.path.join(root, 'a'), os.path.join(root, 'b', 'link'))

shutil.rmtree(root)
