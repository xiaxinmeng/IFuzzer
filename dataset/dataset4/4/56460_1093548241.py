#! /usr/bin/python
import subprocess, sys

# will print err to sys.stderr
subprocess.call(['rmdir', '/no_such_dir'])

# will NOT print err to sys.stderr
subprocess.call(['rmdir', '/no_such_dir'], stdout=sys.stderr)