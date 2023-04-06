if scope == module: check_globals()
else:
  check_locals()
  check_globals()