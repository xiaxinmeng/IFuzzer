fp = open(filename, 'w')
try:
  fp.seek(0, os.SEEK_END)
except OSError as exc:
  if exc.errno != errno.ESPIPE: raise