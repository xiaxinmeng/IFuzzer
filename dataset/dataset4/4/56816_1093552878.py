import subprocess, sys
subprocess.call(["ls", "asda"], stderr = sys.stdout, stdout = open("/dev/null", "w"))