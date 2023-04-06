if locals() is globals(): check_globals()
else:
  check_locals()
  check_globals()