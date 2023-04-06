from concurrent import futures

with futures.ThreadPoolExecutor(max_workers=5) as e:
  e.map(print, range(10))