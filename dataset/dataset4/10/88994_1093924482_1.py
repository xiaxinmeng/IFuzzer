import time, datetime
start = time.time()
end = time.time()

start = datetime.datetime.fromtimestamp(start, None)
end = datetime.datetime.fromtimestamp(end, None)
assert end >= start