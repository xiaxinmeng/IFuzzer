import re
import pickle
import timeit

N = 100000
s = "r = re.compile('[\\udc80-\\udcff]')"
t = timeit.Timer(s, 'import re')
print("%6.2f <- re.compile" % t.timeit(number=N))

s = "r = pickle.loads(p)"
p = pickle.dumps(re.compile('[\udc80-\udcff]'))
t = timeit.Timer(s, 'import pickle; from __main__ import p')
print("%6.2f <- pickle.loads" % t.timeit(number=N))