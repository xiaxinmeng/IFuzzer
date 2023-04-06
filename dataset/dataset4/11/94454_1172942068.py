
if hasattr(os, 'register_at_fork'):
  def close_wakeup_fd():
    signal.set_wakeup_fd(-1)
    self._signal_handlers.clear()

  os.register_at_fork(after_in_child=close_wakeup_fd)
