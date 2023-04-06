
import os
import subprocess

os.chdir(r"\\?\C:\Users")
output = subprocess.check_output("dir", shell=True)
