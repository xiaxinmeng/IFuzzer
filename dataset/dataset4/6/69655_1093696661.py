while not event.is_set():
  do_more_work()
  # Pause because the task is only supposed to happen every X seconds
  # or a wait is in effect due to an error. Do not want to use
  # time.sleep so loop is exited promptly rather than blindly sleeping.
  event.wait(some_amount)
other_work_or_shutdown()