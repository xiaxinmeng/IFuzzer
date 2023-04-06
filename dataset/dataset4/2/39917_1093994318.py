def wait(self):
  """Wait for and return the exit status of the child
process."""
  if self.sts < 0:
    pid, sts = os.waitpid(self.pid, 0)
    if pid == self.pid:
      self.sts = sts
  return self.sts

def _cleanup():
    for inst in _active[:]:
        inst.poll()