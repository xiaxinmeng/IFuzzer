# bisect left on reverse-sorted
pred = lambda y: not (x < y)
idx = bisect_left(a, x, key=pred)

# bisect right on reverse-sorted
pred = lambda y: y < x
idx = bisect_right(a, x, key=pred)