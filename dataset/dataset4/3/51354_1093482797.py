def pause(increment):
  """
  pause or unpause garbage collection.  A positive value
  increases the pause level, while a negative one reduces it.
  when paused, gc won't happen even when explicitly requested with
  gc.collect(), until the pause level drops to 0.
  """