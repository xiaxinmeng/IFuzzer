from difflib import SequenceMatcher
from time import perf_counter as now
xs = 'x'
while True:
    start = now()
    sm = SequenceMatcher(None, xs, xs, autojunk=False)
    r = sm.ratio()
    finish = now()
    print(len(xs), finish - start)
    xs *= 2