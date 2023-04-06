_v = cm.__enter__()
try:
  if hasattr(cm, "__entered__"):
    VAL = cm.__entered__(_v)
  else:
    VAL = _v
  # do stuff
finally:
  cm.__exit__(*exception_status)