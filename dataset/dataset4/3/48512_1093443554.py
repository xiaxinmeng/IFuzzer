import subprocess

data = "if True:\n  pass\n  "
filename = "/tmp/test.py"
fh = open(filename, "w")
fh.write(data)
fh.close()
subprocess.check_call(["python", filename])
subprocess.check_call(["python", "-c", "import test"], cwd="/tmp")
compile(data, filename, "exec")