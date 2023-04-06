import shutil
import venv
import subprocess

shutil.rmtree("venv", ignore_errors=True)
venv.EnvBuilder(with_pip=False, symlinks=True).create("venv")