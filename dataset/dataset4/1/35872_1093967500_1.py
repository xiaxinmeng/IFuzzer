def xzip(*iterables):
    gens = map(generator, *iterables)
    while 1:
        yield tuple( [g.next() for g in gens] )

g = xzip( [1,2,3], range(20), xrange(5), genPrimes
(10), getTimeStamp(), open("fil") )