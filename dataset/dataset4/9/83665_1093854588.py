
import time
import itertools
now = time.time_ns()                                                                          
for x in itertools.count(now):
    assert float(x) / 1e9 == x / 1e9
