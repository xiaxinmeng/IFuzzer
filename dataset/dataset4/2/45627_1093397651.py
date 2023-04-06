f = open(filename)
try:
  process(f)
finally:
  f.close()