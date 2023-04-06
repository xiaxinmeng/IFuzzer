# this SEEMS to leak
l = xrange(10000)
while 1:
        a=[]
        map(a.append, l)
        del a

# this does not 
while 1:
       a=range(10000)
       del a