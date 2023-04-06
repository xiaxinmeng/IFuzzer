runs = 190000, 180000, 10000, 10000

from time import perf_counter as now
xs = []
for r in runs:
    xs.extend(range(r * 320))

t0 = now()
xs.sort()
t1 = now()
print(len(xs), t1 - t0)