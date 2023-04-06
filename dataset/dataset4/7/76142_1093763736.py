from pathlib import Path
import subprocess

subprocess.run([Path('/bin/ls')])  # Works Fine
subprocess.run(Path('/bin/ls'))  # Fails