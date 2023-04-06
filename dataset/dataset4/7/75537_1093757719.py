@contextmanager
def gc_disabled():
  previous_enable_state = gc.disable()
  yield
  gc.set_enable(previous_enable_state)