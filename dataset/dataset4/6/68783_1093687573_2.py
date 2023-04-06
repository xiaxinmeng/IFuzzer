def runcode(self, code):
  class OutWriter:
    pass
  writer = OutWriter()
  writer.write = self.write
  old = sys.stdout
  sys.stdout = writer
  try:
    exec(code, self.locals)
  except SystemExit:
    raise
  except:
    self.showtraceback()
  sys.stdout = old