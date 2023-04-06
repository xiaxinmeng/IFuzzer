timeout = scheduled[0].when - time.monotonic()
events = selector.select(timeout)
process_events(events)
while scheduled:
   if scheduled[0].when > time.monotonic():
      break
   ...