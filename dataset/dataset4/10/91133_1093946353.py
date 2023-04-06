#!/usr/bin/env python3

import os
import tempfile

def createUnremovableDir(workdir):
    print(workdir)
    os.mkdir(f'{workdir}/mydir')
    os.symlink('/bin/bash', f'{workdir}/mydir/mylink') # Symlink to a root owned file
    os.chmod(f'{workdir}/mydir', 0o555)

with tempfile.TemporaryDirectory() as workdir:
    createUnremovableDir(workdir)