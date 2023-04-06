monotonic = None
if hasattr(time, 'clock_gettime'):
  if hasattr(time, 'CLOCK_MONOTONIC_RAW'):
    def monotonic(): return time.clock_gettime(CLOCK_MONOTONIC_RAW)
  else:
    # i don't think that we should expose clock_gettime
    # if CLOCK_MONOTONIC is not available (or the function is useless)
    def monotonic(): return time.clock_gettime(CLOCK_MONOTONIC)
elif os.name == 'nt':
    def monotonic(): return time.clock()
if monotonic is not None:
   monotonic.__doc__ = 'monotonic time'
else:
   del monotonic