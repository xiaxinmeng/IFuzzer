import os
import subprocess
subprocess.Popen(
     "notepad.exe",
     env={"SystemRoot" : os.environ['SystemRoot']}
)