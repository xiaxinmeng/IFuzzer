from itertools import count, islice
irange = lambda start, stop, step: islice(count(start, step), (stop-start+step-1)//step)