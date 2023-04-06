import subprocess, sys
python_path = sys.executable
p = subprocess.Popen([python_path, "-c", "import sys; sys.exit(1)"])
p.wait()
p = subprocess.Popen([python_path, "-c", "import sys; sys.exit(1)"],
                     executable="foo")
p.wait()