if remaining >= 4.0:
    maxDelay = 1
else:
    maxDelay = .05
delay = min(delay * 2, remaining, maxDelay)