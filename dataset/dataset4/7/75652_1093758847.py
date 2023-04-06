import subprocess

import sys

subprocess.Popen([sys.executable, "-c", "pass"], env=BadEnv())