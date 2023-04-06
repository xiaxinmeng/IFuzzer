#!/usr/bin/env python
import pathlib
import subprocess

output = subprocess.check_output(['ps', 'aux'])
pathlib.Path('/tmp/ps_aux.txt').write_bytes(output)