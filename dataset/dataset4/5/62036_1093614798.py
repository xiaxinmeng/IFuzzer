pytb
"""
Traceback (most recent call last):
  File "mp_exception_bug.py", line 8, in <module>
    print p.map(f, [1,2,3])
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 227, in map
    return self.map_async(func, iterable, chunksize).get()
  File "/usr/lib/python2.7/multiprocessing/pool.py", line 528, in get
    raise self._value
NameError: global name 'y' is not defined
"""
