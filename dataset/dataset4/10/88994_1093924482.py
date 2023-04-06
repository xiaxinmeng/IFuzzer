import time, datetime
start = time.time()
end = datetime.datetime.now()

start = datetime.datetime.fromtimestamp(start, None)
assert end >= start # fails about half the time.