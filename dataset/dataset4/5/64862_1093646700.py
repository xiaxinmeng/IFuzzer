from collections import deque
d = deque((0,))
try:
  while True:
        n = d.popleft()
        print(n, len(d))
        if n < 5:
            d.extend((n+1, n+2))
except IndexError:
    pass