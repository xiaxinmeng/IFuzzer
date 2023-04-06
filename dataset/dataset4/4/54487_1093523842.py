wallclock = None
if hasattr(time, 'clock_gettime') and hasattr(time, 'CLOCK_MONOTONIC_RAW'):
  # I understood that CLOCK_MONOTONIC_RAW is more reliable
  # than CLOCK_MONOTONIC, because CLOCK_MONOTONIC may be adjusted
  # by NTP. I don't know if it's correct.
  def wallclock():
    return time.clock_gettime(CLOCK_MONOTONIC_RAW)