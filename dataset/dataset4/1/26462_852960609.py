
with sqlite.connect(path) as cx:
  conn = cx # "reference cycle"
cx.close()
# I expect the DB to be closed at that point even if 'conn' object still exists
