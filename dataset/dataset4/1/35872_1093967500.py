def generator( iterable ):
    for i in iterable:
        yield i

g = generator( [1,2,3,4] )
h = generator( range(10) )
i = generator( xrange(10) )
j = generator( 'abcd' )