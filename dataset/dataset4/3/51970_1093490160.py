from itertools import count, takewhile
irange = lambda start, stop, step: takewhile(lambda x: x<stop, (start+i*step for i in count()))