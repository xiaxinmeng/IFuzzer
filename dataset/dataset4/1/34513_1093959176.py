while 1:
  try:
    line = raw_input()
  except EOFError:
    break
  msg = msg + line