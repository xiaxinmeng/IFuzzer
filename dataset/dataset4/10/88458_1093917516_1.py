with contextlib.ExitStack() as es:
  r = es.enter_context(managed_resource())
  es.pop_all()
  # Uh-oh, r gets released anyway

with contextlib.ExitStack() as es:
  r = es.enter_context(ManagedResource())
  es.pop_all()
  # Works as expected