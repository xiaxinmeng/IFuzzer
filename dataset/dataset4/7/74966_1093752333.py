import os
import subprocess
from contextlib import contextmanager
from tempfile import TemporaryDirectory


def get_python_path():
    return subprocess.check_output(
        ['python', '-c', 'import sys;print(sys.executable)']
    ).decode().strip()


@contextmanager
def temp_chdir(cwd=None):
    with TemporaryDirectory() as d:
        origin = cwd or os.getcwd()
        os.chdir(d)