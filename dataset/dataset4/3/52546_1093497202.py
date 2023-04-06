with gil.cond:
  if gil.n_waiting or gil.locked:
    gil.n_waiting += 1
    while True:
      gil.cond.wait() #always wait at least once
      if not gil.locked:
        break
    gil.n_waiting -= 1
  gil.locked = True