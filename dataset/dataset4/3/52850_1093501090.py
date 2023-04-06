@contextlib.contextmanager
def atomic_write(filename):
  tempname = filename + ".tmp"
  out = open(tempname, "w")
  try:
     yield out
     if hasattr('os', 'fsync'):
        os.fsync(out.fileno())
     out.close()
     if os.name in ('nt', 'ce'):
        os.unlink(filename)
        # ... hope that it doesn't fail here ...
     os.rename(tempname, filename)
  except:
     out.close()
     os.unlink(tempname)
     raise