import subprocess
proc = subprocess.Popen(["gdb", "-nx", "--version"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)