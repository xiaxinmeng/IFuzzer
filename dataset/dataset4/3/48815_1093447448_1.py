# writes increasingly more lines to a file
for N in range(lo, hi, step):
    fp = open('foodata.txt', 'wt')
    start = time.time()
    for i in range( N ):
        fp.write( '%s\n' % i)
    fp.close()
    stop = time.time()
    print ( "%s\t%s" % (N, stop-start) )