# use a single object
lock = ShrdExclLock()

with lock.shared:
  ...

with lock.exclusive:
  ...