for future in finished:
     yield future
     pending.remove(future)  ## KeyError triggered on as_completed( [f,f] )