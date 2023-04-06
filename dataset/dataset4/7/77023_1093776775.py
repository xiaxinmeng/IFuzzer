# current
if timeout is None:
    timeout = -1
elif timeout <= 0:
    timeout = 0

# changed
if timeout is None:
    timeout = -1
elif timeout < -1:
    timeout = 0