def save_overwrite_open(fname):
  try:
    return open(fname,"w")
  except IOError:
    os.unlink(fname)
    return open(fname,"w")