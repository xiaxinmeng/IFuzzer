def heapremove(heap, x):
  i = bisect.bisect_left(heap, x)
  if heap[i] == x:
    del heap[i]
  else:
    raise ValueError