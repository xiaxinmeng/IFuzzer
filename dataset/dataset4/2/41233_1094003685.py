full = open('/dev/full', 'w')
while 1:
    print >>full, 'x' * 1023
    print >>full