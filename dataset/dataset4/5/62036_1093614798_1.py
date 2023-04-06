pytb
"""
Traceback (most recent call last):
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 98, in worker
    result = (True, func(*args, **kwds))
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 67, in mapstar
    return map(*args)
  File "mp_exception_bug.py", line 4, in f
    return x*y
NameError: global name 'y' is not defined

Traceback (most recent call last):
  File "mp_exception_bug.py", line 8, in <module>
    print p.map(f, [1,2,3])
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 231, in map
    return self.map_async(func, iterable, chunksize).get()
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 535, in get
    raise self._value[0]
NameError: global name 'y' is not defined
"""
