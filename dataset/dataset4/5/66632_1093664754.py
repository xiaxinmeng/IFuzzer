import subprocess

def ccall(cmdline, stdout, stderr):
  proc = subprocess.Popen(['python', 'b.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  proc.communicate()
  if proc.returncode != 0: raise subprocess.CalledProcessError(proc.returncode, cmdline)
  return 0