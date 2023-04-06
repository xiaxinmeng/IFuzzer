proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
try:
  return proc.communicate(timeout=1.0)
except TimeoutExpired:
  proc.kill()
  return proc.communicate() # <== HERE